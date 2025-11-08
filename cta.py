import logging
from dotenv import dotenv_values
import requests
from utils import train_timestamp_to_date, bus_timestamp_to_date

logger = logging.getLogger(__name__)
secrets = dotenv_values(".env")

TRAIN_ARRIVALS_ENDPOINT = "https://lapi.transitchicago.com/api/1.0/ttarrivals.aspx"
TRAIN_LOCATIONS_ENDPOINT = "https://lapi.transitchicago.com/api/1.0/ttpositions.aspx"
BUS_PREDICTIONS_ENDPOINT = "https://www.ctabustracker.com/bustime/api/v3/getpredictions"


def create_eta_arr(train, eta_json):
    """
    Returns the arrival ETA from the ETA JSON returned from the API
    """
    eta_arr = []
    logger.debug(f"ETA JSON: {eta_json}")
    for eta in eta_json:
        if train:
            eta_arr.append(train_timestamp_to_date(eta['arrT']))
        else:
            eta_arr.append(bus_timestamp_to_date(eta['prdtm']))
    logger.debug(f"ETA Arrivals: {eta_arr}")
    return eta_arr


def get_train_arrivals(stpid):
    """
    Calls the CTA train API to get the arrivals for a given stop
    and returns an array of the all of the arrivals ETAs in order
    """
    url = f"{TRAIN_ARRIVALS_ENDPOINT}?stpid={stpid}&max=3&key={secrets.get('TRAIN_API_KEY')}&outputType=JSON"
    response = requests.get(url)
    ctatt = response.json()['ctatt']
    if 'eta' not in ctatt:
        return []
    return create_eta_arr(True, ctatt['eta'])


def get_bus_arrivals(stpid):
    """
    Calls the CTA bus API to get the arrivals for a given stop
    and returns an array of the all of the arrivals ETAs in order
    """
    url = f"{BUS_PREDICTIONS_ENDPOINT}?key={secrets.get('BUS_API_KEY')}&stpid={stpid}&top=3&format=json"
    response = requests.get(url)
    eta = response.json()['bustime-response']['prd']
    if len(eta) == 0:
        return []
    return create_eta_arr(False, eta)


def get_train_lines():
    """
    Retrieves the location of all live trains on given routes
    """
    lines = secrets.get("TRAIN_LINES")
    url = f"{TRAIN_LOCATIONS_ENDPOINT}?key={secrets.get('TRAIN_API_KEY')}&outputType=JSON&rt={lines}"
    response = requests.get(url)
    return response.json()['ctatt']['route']


def get_train_1_north():
    return get_train_arrivals(secrets.get("TRAIN_1_NORTH_STPID"))


def get_train_1_south():
    return get_train_arrivals(secrets.get("TRAIN_1_SOUTH_STPID"))


def get_train_2_north():
    return get_train_arrivals(secrets.get("TRAIN_2_NORTH_STPID"))


def get_train_2_south():
    return get_train_arrivals(secrets.get("TRAIN_2_SOUTH_STPID"))


def get_bus_1_west():
    return get_bus_arrivals(secrets.get("BUS_1_WEST_STPID"))


def get_bus_1_east():
    return get_bus_arrivals(secrets.get("BUS_1_EAST_STPID"))
