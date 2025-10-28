import logging
import time
import threading
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from dotenv import dotenv_values
from icons import icons
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
from colours import RED_LINE_COLOUR, PURPLE_LINE_COLOUR, ORANGE_LINE_COLOUR, BLUE_LINE_COLOUR, GREEN_LINE_COLOUR, DIVVY_COLOUR, BUS_COLOUR, TEXT_COLOUR, get_colour

secrets = dotenv_values(".env")
logger = logging.getLogger(__name__)


class TransitDisplay:
    def __init__(self):
        # Configure RGB matrix
        options = RGBMatrixOptions()
        options.rows = 64
        options.cols = 64
        options.chain_length = 1
        options.parallel = 1
        options.hardware_mapping = 'regular'
        options.gpio_slowdown = 4
        options.brightness = int(secrets.get("BRIGHTNESS"))
        options.disable_hardware_pulsing = 1

        self.matrix = RGBMatrix(options=options)
        self.canvas = self.matrix.CreateFrameCanvas()

        self.last_api_call = 0
        self.api_interval = 30  # API calls every 30 seconds
        self.display_interval = 15  # Display refresh every 15 seconds
        self.last_display_update = 0
        self.last_transit_call = 0  # Track transit API calls separately
        self.transit_interval = 120  # Transit API calls every 2 minutes

        self.icons = icons

        self.font = graphics.Font()
        self.font.LoadFont("fonts/5x8.bdf")

        # Sleep mode
        self.sleep_mode_enabled = secrets.get("SLEEP_MODE_ENABLED") == "True"
        self.sleep_mode_start = datetime.strptime(secrets.get("SLEEP_MODE_START"), "%H:%M").time()
        self.sleep_mode_end = datetime.strptime(secrets.get("SLEEP_MODE_END"), "%H:%M").time()

        # Store API data
        self.api_data = {}
        self.api_lock = threading.Lock()

        # Get configurable train colours from .env
        self.train_1_colour = get_colour(secrets.get("TRAIN_1_COLOUR"))
        self.train_2_colour = get_colour(secrets.get("TRAIN_2_COLOUR"))

    def draw_icon(self, icon_name, x, y, color):
        if icon_name not in self.icons:
            return

        icon_bitmap = self.icons[icon_name]
        for row_idx, row in enumerate(icon_bitmap):
            for col_idx, pixel in enumerate(row):
                if pixel == 1:
                    self.canvas.SetPixel(
                        x + col_idx, y + row_idx, color.red, color.green, color.blue)

    def draw_line(self, x_start, x_end, y_start, y_end, colour):
        if x_start == x_end:
            for y in range(y_start, y_end):
                self.canvas.SetPixel(x_start, y, colour.red,
                                     colour.green, colour.blue)
        elif y_start == y_end:
            for x in range(x_start, x_end):
                self.canvas.SetPixel(x, y_start, colour.red,
                                     colour.green, colour.blue)

    def draw_question_mark_if_unknown(self, value, pos_x, pos_y):
        """Helper to draw a question mark if value is unknown/empty"""
        if not value or (isinstance(value, list) and len(value) == 0):
            self.draw_icon('question_mark', pos_x, pos_y, TEXT_COLOUR)
            return True
        return False

    def draw_sleep_mode(self):
        # Draw a single green pixel at 25 brightness in the bottom left corner
        # Bottom left is (0, 63) since rows are 0-63
        # A single pixel as a means of a status indicator
        self.canvas.Clear()

        self.matrix.brightness = 25

        green_color = graphics.Color(0, 25, 0)
        self.canvas.SetPixel(0, 63, green_color.red, green_color.green, green_color.blue)

        self.canvas = self.matrix.SwapOnVSync(self.canvas)
        return True

    def should_fetch_transit_times(self):
        """
        Check if we should fetch transit times based on time and day
        This is necessary to work around the 1,500 calls a month limit
        """
        now = datetime.now()
        # Check if it's a weekday (0=Monday, 4=Friday)
        is_weekday = now.weekday() < 5
        # Check if it's between 6am and 8am
        is_rush_hour = 6 <= now.hour < 8
        return is_weekday and is_rush_hour

    def fetch_api_data(self):
        """Fetch all API data in parallel using ThreadPoolExecutor"""
        from cta import (get_train_1_north, get_train_1_south,
                         get_train_2_north, get_train_2_south,
                         get_bus_1_west, get_bus_1_east, get_train_routes)
        from divvy import get_specific_divvy_station_status, get_nearby_ebikes
        from transit import get_time_to_office, get_time_to_love
        from utils import minutes_until_eta

        current_time = time.time()

        api_functions = {
            'train_1_north': get_train_1_north,
            'train_1_south': get_train_1_south,
            'train_2_north': get_train_2_north,
            'train_2_south': get_train_2_south,
            'bus_1_west': get_bus_1_west,
            'bus_1_east': get_bus_1_east,
            'divvy_specific_station': get_specific_divvy_station_status,
            'divvy_nearby_ebikes': get_nearby_ebikes,
            'locations': get_train_routes
        }

        # Check if we should fetch transit times
        should_fetch_transit = (
            self.should_fetch_transit_times() and
            current_time - self.last_transit_call >= self.transit_interval
        )

        if should_fetch_transit:
            api_functions['time_to_office'] = get_time_to_office
            api_functions['time_to_love'] = get_time_to_love
            self.last_transit_call = current_time

        # Execute all API calls in parallel
        with ThreadPoolExecutor(max_workers=len(api_functions)) as executor:
            future_to_key = {executor.submit(
                func): key for key, func in api_functions.items()}

            results = {}
            for future in future_to_key:
                key = future_to_key[future]
                try:
                    results[key] = future.result()
                except Exception as e:
                    logger.error(f"Error fetching {key}: {e}")
                    results[key] = None

        # Set default values for transit times if not fetched
        if not should_fetch_transit or results['time_to_love'] != 0 or results['time_to_office'] != 0:
            results['time_to_love'] = 4 + \
                minutes_until_eta(results['train_1_south']) + 17 + 3
            results['time_to_office'] = 4 + \
                minutes_until_eta(results['train_1_south']) + 23 + 6

        # Update shared data with lock
        with self.api_lock:
            self.api_data = results

        logger.info("API data updated")

    def draw_transit_etas(self):
        """Update the display with current data - draws ETA times for all transit options"""
        from utils import minutes_until_eta

        # Access shared data with lock
        with self.api_lock:
            data = self.api_data.copy()

        # Train 1 Row
        # Draw train 1 south ETA
        train_1_south_data = data.get('train_1_south', [])
        if not self.draw_question_mark_if_unknown(train_1_south_data, 25, 8):
            minutes = minutes_until_eta(train_1_south_data)
            graphics.DrawText(self.canvas, self.font, 25, 15,
                              self.train_1_colour, str(minutes))

        # Draw train 1 north ETA
        train_1_north_data = data.get('train_1_north', [])
        if not self.draw_question_mark_if_unknown(train_1_north_data, 46, 8):
            minutes = minutes_until_eta(train_1_north_data)
            graphics.DrawText(self.canvas, self.font, 46, 15,
                              self.train_1_colour, str(minutes))

        # Train 2 Row
        # Draw train 2 south ETA
        train_2_south_data = data.get('train_2_south', [])
        if not self.draw_question_mark_if_unknown(train_2_south_data, 25, 19):
            minutes = minutes_until_eta(train_2_south_data)
            graphics.DrawText(self.canvas, self.font, 25, 26,
                              self.train_2_colour, str(minutes))

        # Draw train 2 north ETA
        train_2_north_data = data.get('train_2_north', [])
        if not self.draw_question_mark_if_unknown(train_2_north_data, 46, 19):
            minutes = minutes_until_eta(train_2_north_data)
            graphics.DrawText(self.canvas, self.font, 46, 26,
                              self.train_2_colour, str(minutes))

        # Bus Row
        # Draw bus west ETA
        bus_west_data = data.get('bus_1_west', [])
        if not self.draw_question_mark_if_unknown(bus_west_data, 25, 31):
            minutes = minutes_until_eta(bus_west_data)
            graphics.DrawText(self.canvas, self.font, 25,
                              38, BUS_COLOUR, str(minutes))

        # Draw bus east ETA
        bus_east_data = data.get('bus_1_east', [])
        if not self.draw_question_mark_if_unknown(bus_east_data, 46, 31):
            minutes = minutes_until_eta(bus_east_data)
            graphics.DrawText(self.canvas, self.font, 46,
                              38, BUS_COLOUR, str(minutes))

        # Divvy Row
        # Draw Dvvy Station status (regular bikes, ebikes)
        divvy_station_data = data.get('divvy_specific_station', [])
        if not self.draw_question_mark_if_unknown(divvy_station_data, 23, 49):
            # divvy_station_data is [regular_bikes, ebikes]
            regular_bikes = divvy_station_data[0] if len(
                divvy_station_data) > 0 else 0
            ebikes = divvy_station_data[1] if len(
                divvy_station_data) > 1 else 0
            graphics.DrawText(self.canvas, self.font, 23, 49,
                              TEXT_COLOUR, str(regular_bikes))
            graphics.DrawText(self.canvas, self.font, 41,
                              49, TEXT_COLOUR, str(ebikes))

        # Draw nearby ebikes count
        nearby_ebikes_data = data.get('divvy_nearby_ebikes')
        if nearby_ebikes_data is not None:
            graphics.DrawText(self.canvas, self.font, 52, 49,
                              TEXT_COLOUR, str(nearby_ebikes_data))

        # Locations Row
        # Draw time to office
        time_to_office = data.get('time_to_office')
        if time_to_office is not None and time_to_office > 0:
            graphics.DrawText(self.canvas, self.font, 21, 59,
                              TEXT_COLOUR, str(time_to_office))
        else:
            self.draw_question_mark_if_unknown([], 21, 59)

        # Draw time to love location
        time_to_love = data.get('time_to_love')
        if time_to_love is not None and time_to_love > 0:
            graphics.DrawText(self.canvas, self.font, 48, 59,
                              TEXT_COLOUR, str(time_to_love))
        else:
            self.draw_question_mark_if_unknown([], 48, 59)

    def draw_train_positions(self):
        from cta_stations import stations
        # Access shared data with lock
        with self.api_lock:
            data = self.api_data.copy()

        trains = {}
        for route in data.get('locations'):
            if route['@name'] == "red":
                trains['red'] = route['train']
            elif route['@name'] == "blue":
                trains['blue'] = route['train']
            elif route['@name'] == "g":
                trains['green'] = route['train']
            elif route['@name'] == "org":
                trains['orange'] = route['train']

        # Train tracker handling
        for train in trains['red']:
            if train['destNm'] == "Howard":
                self.draw_icon(
                    'train_up', 1, 60 - (stations[train['nextStaId']]['red_order_north'] / 32 * 58), TEXT_COLOUR)
            else:
                self.draw_icon(
                    'train_down', 1, 2 + (stations[train['nextStaId']]['red_order_south'] / 32 * 57), TEXT_COLOUR)
        for train in trains['blue']:
            if train['destNm'] == "O'Hare":
                self.draw_icon(
                    'train_up', 60, 60 - (stations[train['nextStaId']]['blue_order_north'] / 32 * 58), TEXT_COLOUR)
            else:
                self.draw_icon(
                    'train_down', 60, 2 + (stations[train['nextStaId']]['blue_order_south'] / 32 * 57), TEXT_COLOUR)
        for train in trains['green']:
            if train['destNm'] == "Harlem/Lake":
                self.draw_icon(
                    'train_left', 60 - (stations[train['nextStaId']]['green_order_north'] / 26 * 58), 60, TEXT_COLOUR)
            else:
                self.draw_icon(
                    'train_right', 2 + (stations[train['nextStaId']]['green_order_south'] / 26 * 57), 60, TEXT_COLOUR)
        for train in trains['orange']:
            if train['destNm'] == "Loop":
                self.draw_icon(
                    'train_right', 61 - (stations[train['nextStaId']]['orange_order_north'] / 12 * 57), 1, TEXT_COLOUR)
            else:
                self.draw_icon(
                    'train_left', 61 - (stations[train['nextStaId']]['orange_order_south'] / 11 * 57), 1, TEXT_COLOUR)

    def update_display(self):
        """Update the display with icons and data"""
        self.canvas.Clear()

        # Draw transit icons with proper positioning
        # Train 1 Row
        self.draw_icon('train', 7, 7, self.train_1_colour)
        self.draw_icon('down_arrow', 18, 9, self.train_1_colour)
        self.draw_icon('up_arrow', 39, 9, self.train_1_colour)

        # Train 2 Row
        self.draw_icon('train', 7, 18, self.train_2_colour)
        self.draw_icon('down_arrow', 18, 20, self.train_2_colour)
        self.draw_icon('up_arrow', 39, 20, self.train_2_colour)

        # Bus Row
        self.draw_icon('bus', 7, 30, BUS_COLOUR)
        self.draw_icon('left_arrow', 18, 32, BUS_COLOUR)
        self.draw_icon('right_arrow', 39, 32, BUS_COLOUR)

        # Divvy Row
        self.draw_icon('bike', 5, 40, DIVVY_COLOUR)
        self.draw_icon('bolt', 32, 42, DIVVY_COLOUR)

        # Locations Row
        self.draw_icon('office', 10, 52, graphics.Color(118, 66, 0))
        self.draw_icon('heart', 34, 52, graphics.Color(255, 0, 0))
        #
        # Draw all the ETA data
        self.draw_transit_etas()

        # Draw Train Lines
        self.draw_line(2, 2, 2, 61, RED_LINE_COLOUR)
        self.draw_line(2, 60, 61, 61, GREEN_LINE_COLOUR)
        self.draw_line(61, 61, 3, 61, BLUE_LINE_COLOUR)
        self.draw_line(3, 61, 2, 2, ORANGE_LINE_COLOUR)
        self.draw_train_positions()

        self.canvas = self.matrix.SwapOnVSync(self.canvas)

    def run(self):
        try:
            while True:
                current_time = time.time()
                current_rel_time = datetime.now().time()
                if self.sleep_mode_enabled and (current_rel_time > self.sleep_mode_start or current_rel_time < self.sleep_mode_end):
                    self.draw_sleep_mode()
                    # Sleep 60s if sleep mode is active and don't make API calls
                    time.sleep(60)
                    continue

                # Fetch API data every 30 seconds
                if current_time - self.last_api_call >= self.api_interval:
                    logger.info("Fetching API data...")
                    self.fetch_api_data()
                    self.last_api_call = current_time

                # Update display every 15 seconds
                if current_time - self.last_display_update >= self.display_interval:
                    logger.info("Updating display...")
                    self.update_display()
                    self.last_display_update = current_time

                # Sleep briefly to prevent busy waiting
                time.sleep(0.5)

        except KeyboardInterrupt:
            logger.info("Shutting down")
        finally:
            self.matrix.Clear()
