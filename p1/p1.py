# Jordan Streete, 04/08/2021
"""
Coding Task #1- Develop a simple Linux CLI application that toggles gpio X based on the input from gpio Y.

NOTES:
    - As gpiozero is a higher level interface, inputs are classed as "Button" and outputs are classed as "LED"
    - I've opted not to use type hints and instead put the types in the docstrings because type hints are a very new feature in python, and would probably break something in older versions
    - I would like to use sysfs to get the highest possible pin number to moderate/protect against bad user input, but I couldn't figure out how (as of now)
    - To run as a script (i.e. not a service) run like this: python3 p1.py -i Y -o X [OPTIONALS]
    - I created the systemd file, however I haven't had a chance to test it properly as I don't have a raspberry pi or anything on hand to test it on. I'm not sure, but I don't think testing it as a service works under emulation (like the pins do)
"""

from gpiozero import LED, Button
import argparse
import datetime
from time import sleep


def retrieve_state(y, x, log_active):
    """
    Retrieves the state of gpio Y and, based on that state, passes gpio X to the correct function.

    y, x -> int, int
    log_active -> bool
    """
    input_pin = Button(y)
    output_pin = LED(x)

    state_active = input_pin.is_pressed

    if log_active:
        log(state_active, y)

    if state_active:
        y_high(output_pin)
    else:
        y_low(output_pin)

    return state_active


def y_high(output_pin, n=5):
    """
    Toggles gpio x LOW-HIGH-LOW-HIGH... at 1 second intervals (as per the requirements of the problem if gpio y is HIGH). I've implemented an exit condition to restrict the number of blinks. The for loop can be replaced by a while True to make it blink for an infinite amount of time.

    x -> LED
    n -> int
    """
    for _ in range(n):
        output_pin.off()
        sleep(1)
        output_pin.on()
        sleep(1)


def y_low(output_pin):
    """
    Toggles gpio x LOW (as per the requirements of the problem if gpio y is LOW).

    x -> LED
    """
    output_pin.off()


def log(is_pressed, y):
    """
    Recieves the state of gpio Y and appends it, along with the date and time in UTC, to a log file named 'log.txt'.
    I decided to use UTC as it would be consistent worldwide, and the problem didn't specify one to use.
    This function is only called if the '--log' flag is used.

    is_pressed -> bool
    y -> int
    """
    now = datetime.datetime.now(datetime.timezone.utc)

    with open("log.txt", "a") as logfp:
        logfp.write(
            f"{now :%y-%m-%d}T{now :%H:%M:%S} gpio {y} {'HIGH' if (is_pressed == True) else 'LOW'}\n"
        )


def main():
    parser = argparse.ArgumentParser(
        description="A simple Linux CLI application that toggles gpio X based on the input from gpio Y"
    )

    parser.add_argument(
        "-i",
        help="Input pin, internally recognized as 'gpio y' or 'input_pin'",
        type=int,
        required=True,
    )
    parser.add_argument(
        "-o",
        help="Output pin, internally recognized as 'gpio x' or 'output_pin'",
        type=int,
        required=True,
    )
    parser.add_argument(
        "--log", help="Log input (Y) pin state in a text file", action="store_true"
    )

    args = parser.parse_args()

    retrieve_state(args.i, args.o, args.log)


if __name__ == "__main__":
    main()
