import logging
import requests
import numpy as np
from dotenv import dotenv_values

logger = logging.getLogger(__name__)

secrets = dotenv_values(".env")

DIVVY_STATION_STATUS_ENDPOINT = "https://gbfs.lyft.com/gbfs/2.3/chi/en/station_status.json"
DIVVY_FREE_BIKE_ENDPOINT = "https://gbfs.lyft.com/gbfs/2.3/chi/en/free_bike_status.json"

BIKE_VEHICLE_ID = "1"
EBIKE_VEHICLE_ID = "2"


def get_station_status(station_id):
    """
    Returns JSON object on the status of a station
    """
    response = requests.get(DIVVY_STATION_STATUS_ENDPOINT)
    stations = response.json()['data']['stations']
    for station in stations:
        if station["station_id"] == station_id:
            logger.debug(f"Divvy Station: {station}")
            return station
    return None


def parse_station_vehicles(vehicles):
    """
    Returns an array containing the amount of regular bikes followed by ebikes
    """
    available_vehicles = [0, 0]
    for vehicle_type in vehicles:
        if vehicle_type['vehicle_type_id'] == BIKE_VEHICLE_ID:
            available_vehicles[0] = vehicle_type['count']
        elif vehicle_type['vehicle_type_id'] == EBIKE_VEHICLE_ID:
            available_vehicles[1] = vehicle_type['count']
    return available_vehicles


def calculate_distances_to_point(bikes, target_lat, target_lon):
    """
    Calculates the distance from each bike to a target point using vectorized Haversine formula.
    Returns a numpy array of distances in meters for each bike.
    """
    # Extract all lat/lon values into arrays (fast list comprehension)
    lats = np.array([b['lat'] for b in bikes], dtype=np.float64)
    lons = np.array([b['lon'] for b in bikes], dtype=np.float64)

    # Convert to radians (vectorized operation)
    lat1 = np.radians(target_lat)
    lon1 = np.radians(target_lon)
    lat2 = np.radians(lats)
    lon2 = np.radians(lons)

    # Haversine formula (all operations vectorized across entire array)
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = np.sin(dlat / 2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))

    # Earth radius in meters
    R = 6371000
    distances = R * c

    return distances


def get_nearby_ebikes():
    """
    Returns the integer count of ebikes within the specified radius of a target point.
    """
    response = requests.get(DIVVY_FREE_BIKE_ENDPOINT)
    bikes = response.json()['data']['bikes']

    if not bikes:
        return 0

    # Filter for only ebikes
    ebikes = [bike for bike in bikes if bike['vehicle_type_id'] == EBIKE_VEHICLE_ID]

    if not ebikes:
        return 0

    # Calculate distances to all ebikes
    distances = calculate_distances_to_point(ebikes, float(
        secrets.get("HOME_LAT")), float(secrets.get("HOME_LONG")))

    # Count ebikes within radius
    nearby_count = np.sum(distances <= secrets.get(
        "NEARBY_BIKE_RADIUS_METERS"))
    return int(nearby_count)


def get_winthrop_lawrence_status():
    """
    Returns an array containing the amount of regular bikes followed by ebikes
    """
    station_status = get_station_status(secrets.get("DIVVY_STATION_ID"))
    return parse_station_vehicles(station_status['vehicle_types_available'])
