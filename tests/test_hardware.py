""" Provide a set of tests cases to demonstrate a basic device that meets
wasatch needs. This includes simple blocking and long polling separate process
devices.
"""

import time
import pytest

from autofalloff import zaber_control, oct_hardware, simulated

ZABERS_COMPORT = "COM4"
REFARM_COMPORT = "COM3"

class TestSimulatedDevices:
    def test_simulated_refarm_status(self, caplog):
        refarm = simulated.RefArmControl(REFARM_COMPORT)
        status = refarm.get_version()
        assert status == "Ver:1.5I\r\nA"

    def test_simulated_zaber_status(self, caplog):
        zaber = simulated.ZaberControl(ZABERS_COMPORT)
        status = zaber.getStatus()

        assert status == "idle"

@pytest.mark.skipif(not pytest.config.getoption("--hardware"),
                    reason="need --hardware option to run")
class TestRefArmControl:
    def test_refarmcontrol_device_get_status(self, caplog):
        refarm = oct_hardware.RefArmControl(REFARM_COMPORT)
        status = refarm.get_version()
        assert status != None
        assert status == "Ver:1.5I\r\nA"

    def test_hwl_position_home_90_home(self, caplog):
        refarms = oct_hardware.RefArmControl(REFARM_COMPORT)

        move_duration = 2.0
        result = refarms.hwl_home()
        assert result == "A\r\n"
        time.sleep(move_duration)

        result = refarms.hwl_relative(90)
        assert result == "A\r\n"
        time.sleep(move_duration)

        result = refarms.hwl_home()
        assert result == "A\r\n"

    def test_qwl_position_home_90_home(self, caplog):
        refarms = oct_hardware.RefArmControl(REFARM_COMPORT)

        move_duration = 2.0
        result = refarms.qwl_home()
        assert result == "A\r\n"
        time.sleep(move_duration)

        result = refarms.qwl_relative(90)
        assert result == "A\r\n"
        time.sleep(move_duration)

        result = refarms.qwl_home()
        assert result == "A\r\n"


@pytest.mark.skipif(not pytest.config.getoption("--hardware"),
                    reason="need --hardware option to run")
class TestZaberDevice:
    def test_zaber_device_get_status(self, caplog):
        motor = zaber_control.ZaberControl(ZABERS_COMPORT)
        status = motor.getStatus()

        assert status != None

    def test_zaber_device_can_home(self, caplog):
        motor = zaber_control.ZaberControl(ZABERS_COMPORT)
        motor.homeMotor()
        time.sleep(4)


    def test_position_cycle(self, caplog):
        mm_stops = [0.1, 0.5, 1, 1.5, 2, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0,
                    5.5, 6.0, 6.5, 7.0]
        step_size = 21428.5714

        stop_interval = 0.3
        motor = zaber_control.ZaberControl(ZABERS_COMPORT)
        motor.homeMotor()
        time.sleep(3)

        for stop in mm_stops:
            micro_steps = stop * step_size
            print "Move to absolute position: %s" % micro_steps
            motor.setPositionAbsolute(micro_steps)
            time.sleep(stop_interval)

