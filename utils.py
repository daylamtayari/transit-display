import logging
from datetime import datetime
from math import floor
from dotenv import dotenv_values

logger = logging.getLogger(__name__)
secrets = dotenv_values(".env")


def train_timestamp_to_date(timestamp):
    """
    Converts a timestamp from the CTA train API into a datetime object
    """
    return datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S')


def bus_timestamp_to_date(timestamp):
    """
    Converts a timestamp from the CTA bus API into a datetime object
    """
    return datetime.strptime(timestamp, '%Y%m%d %H:%M')


def minutes_until_date(date_timestamp):
    """
    Returns the amount of minutes until a datetime object, rounded down
    """
    delta = date_timestamp - datetime.now()
    return floor(delta.total_seconds() / 60)


def minutes_until_eta(eta, i=0):
    """
    Returns the amount of minutes until an arrival, using the following
    arrival if the time until the arrival is under the configured cutoff,
    unless there is no additional arrival
    """
    cutoff = int(secrets.get("MINUTES_UNTIL_ETA_CUTOFF", 5))
    minutes = minutes_until_date(eta[i])
    logger.debug(f"Minutes until ETA: {minutes}")
    # If time is under cutoff and there's another arrival, show time until next arrival instead
    if minutes < cutoff and len(eta) > 1:
        return minutes_until_date(eta[i+1])
    return minutes
