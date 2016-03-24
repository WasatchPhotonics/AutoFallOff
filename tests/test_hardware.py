""" Provide a set of tests cases to demonstrate a basic device that meets
wasatch needs. This includes simple blocking and long polling separate process
devices.
"""

import time
import pytest

from autofalloff import zaber_control
COM_PORT = "COM4"

@pytest.mark.skipif(not pytest.config.getoption("--hardware"),
                    reason="need --hardware option to run")
class TestZaberDevice:
    def test_zaber_device_get_status(self, caplog):
        motor = zaber_control.ZaberControl(COM_PORT)
        status = motor.getStatus()

        assert status != None

    def test_zaber_device_can_home(self, caplog):
        motor = zaber_control.ZaberControl(COM_PORT)
        motor.homeMotor()


    def test_position_cycle(self, caplog):
        mm_stops = [0.1, 0.5, 1, 1.5, 2, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0,
                    5.5, 6.0, 6.5, 7.0]
        step_size = 21428.5714

        stop_interval = 0.3
        motor = zaber_control.ZaberControl(COM_PORT)
        motor.homeMotor()
        time.sleep(3)

        for stop in mm_stops:
            micro_steps = stop * step_size
            print "Move to absolute position: %s" % micro_steps
            motor.setPositionAbsolute(micro_steps)
            time.sleep(stop_interval)

