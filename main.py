import logging
from display import TransitDisplay

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)


def main():
    display = TransitDisplay()
    display.run()


if __name__ == "__main__":
    main()
