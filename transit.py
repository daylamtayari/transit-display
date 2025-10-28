import logging
import requests
import math
from dotenv import dotenv_values


logger = logging.getLogger(__name__)

secrets = dotenv_values(".env")

TRANSIT_PLAN_ENDPOINT = "https://external.transitapp.com/v3/otp/plan"


def get_time_to_loc(dest_lat, dest_long):
    """
    Queries the transit API for the duration between the home location
    and a given location, specified by its coordinates
    """
    response = requests.get(f"{TRANSIT_PLAN_ENDPOINT}?fromPlace={secrets.get('HOME_LAT')},{secrets.get('HOME_LONG')}&toPlace={dest_lat},{dest_long}&numItineraries=1",
                            headers={"apiKey": secrets.get('TRANSIT_API_KEY')})
    logger.debug(response)
    if response.status_code != 200:
        logger.error(f"Error calling Transit API: Status Code {response.status_code}")
        return 0
    if not response.json()['plan']:
        return 0
    # Uses the first returned itinerary
    duration = response.json()['plan']['itineraries'][0]['duration']
    return math.floor(duration / 60)


def get_time_to_office():
    return get_time_to_loc(secrets.get("OFFICE_LAT"), secrets.get("OFFICE_LONG"))


def get_time_to_love():
    return get_time_to_loc(secrets.get("LOVE_LAT"), secrets.get("LOVE_LONG"))
