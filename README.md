# Transit Display

64x64 LED matrix display that shows transit and commute ETAs using CTA, Divvy, and Transit App APIs.

By default, it has three rows of ETA data showing ETAs for both directions of two trains and one bus line. It then has info on the amount of ebikes and regular bikes at the nearest Divvy station as well as ebikes parked in a set radius around. On the last row is ETAs to two locations, by default the office and a partner's home.

Bordering the ETAs are four lines, each representing different train lines, and little arrows representing trains going into a particular direction. Trains are placed on the line proportional to where they are on the path.

## Features
- Train and bus ETAs
- Divvy station status
- Divvy ebikes around a set radius
- Full ETA to specific locations using the Transit app APIs
- Live train map on the border
- Sleep mode to allow for the display to be off between certain hours
- Configuration fully managed by the `.env` configuration file

## Build
- Raspberry Pi
- 64x64 LED RGB matrix ([I used this one from Amazon](https://www.amazon.com/dp/B0BYJHMFSQ/))
- 5V 4A AC to DC power supply
- Micro USB power supply (for the Pi)
- Power strip (optional, simply to reduce the amount of plugs)
- Any mounting hardware you wish to use

## Setup
1. Request API keys for CTA train tracker, bus tracker, and the Transit API
2. Copy `env.tmpl` to `.env` and complete all of the values
3. Install all pip dependencies specified in `requirements.txt`
4. Test the installation by running `python main.py`
5. Create and enable the systemd service using the service files
6. Add the update script to your `crontab` at the desired frequency

## License

This project is licensed under GNU GPLv3
