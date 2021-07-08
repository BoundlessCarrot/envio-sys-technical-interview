# Jordan Streete, 07/07/2021

from gpiozero.pins.mock import MockFactory
from gpiozero import LED, Device
import unittest
import time

from p1 import retrieve_state, y_high, y_low

Device.pin_factory = MockFactory()


class p1_test(unittest.TestCase):
    def test_output_for_input_low(self):
        output_device = LED(9)
        output_device.on()
        y_low(output_device)

        self.assertEqual(output_device.value, 0)

    def test_output_for_input_high(self):
        output_device = LED(11)
        output_device.on()

        state_list = []

        y_high(output_device)
        t_end = time.time() + 2
        while time.time() < t_end:
            state_list.append(output_device.value)
            time.sleep(1)

        # Number of seconds corresponds to the number of blinks
        self.assertEqual(sum(state_list), 2)

    def test_retrieve_state_low(self):
        # Default state is low
        self.assertEqual(retrieve_state(3, 5, True), 0)

    # This unit test requires that the state of the input device be set to high
    # However, the input device gets initialized in the function, which means it cannot be set here as each pin can only be used at one time
    # def test_retrieve_state_high(self):
    #     input_device = Button(3)
    #     input_device.pin.drive_low()
    #     self.assertEqual(retrieve_state(3, 5, True), 1)


if __name__ == "__main__":
    unittest.main()
