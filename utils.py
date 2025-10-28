import logging
from datetime import datetime
from math import floor

logger = logging.getLogger(__name__)


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


def minutes_until_eta(eta):
    """
    Returns the amount of minutes until an arrival, using the following
    arrival if the time until the arrival is under 2 minutes,
    unless there is no additional arrival
    """
    minutes = minutes_until_date(eta[0])
    logger.debug(f"Minutes until ETA: {minutes}")
    # If time is under 2 minutes and there's another arrival, show time until next arrival instead
    if minutes < 2 and len(eta) > 1:
        return minutes_until_date(eta[1])
    return minutes
