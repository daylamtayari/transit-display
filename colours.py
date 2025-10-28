from rgbmatrix import graphics
from dotenv import dotenv_values

secrets = dotenv_values(".env")

# CTA Colours
# https://www.transitchicago.com/developers/branding/
RED_LINE_COLOUR = graphics.Color(227, 55, 25)
PURPLE_LINE_COLOUR = graphics.Color(73, 47, 146)
ORANGE_LINE_COLOUR = graphics.Color(244, 120, 54)
BLUE_LINE_COLOUR = graphics.Color(0, 157, 220)
GREEN_LINE_COLOUR = graphics.Color(0, 169, 79)
BROWN_LINE_COLOUR = graphics.Color(118, 66, 0)
PINK_LINE_COLOUR = graphics.Color(243, 139, 185)
YELOW_LINE_COLOUR = graphics.Color(255, 232, 0)

# Divvy Brand Colour
DIVVY_COLOUR = graphics.Color(47, 178, 230)

# Custom colour for buses
BUS_COLOUR = graphics.Color(int(secrets.get("BUS_COLOUR_RED")), int(secrets.get("BUS_COLOUR_GREEN")), int(secrets.get("BUS_COLOUR_BLUE")))

# White colour for text
TEXT_COLOUR = graphics.Color(255, 255, 255)


# Helper function to get colour by variable name from .env
def get_colour(colour_name):
    """
    Returns the colour object based on the variable name string.
    Used to dynamically select colours from .env
    Defaults to TEXT_COLOUR if not found
    """
    return globals().get(colour_name, TEXT_COLOUR)
