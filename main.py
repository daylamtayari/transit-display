import logging
from display import TransitDisplay

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    display = TransitDisplay()
    display.run()


if __name__ == "__main__":
    main()
