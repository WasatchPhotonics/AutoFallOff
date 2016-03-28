""" Support for various devices that are used in Wasatch Photonics OCT
Engine products.
"""

import sys
import time
import serial
import logging

log = logging.getLogger(__name__)

class SimulatedRefArm(object):
    """ Provide a bare-bones simulation interface with sleep delays to mimic
    actual hardware responses.
    """
    def __init__(self, com_port):
        log.debug("%s setup", self.__class__.__name__)

        self.version = "Ver:1.5I\r\nA"
        self.mimic_delay = 1.0

    def get_version(self):
        time.sleep(self.mimic_delay)
        return self.version

class SimulatedZaber(object):
    """ Provide a bare-bones simulation interface with sleep delays to mimic
    actual hardware responses.
    """
    def __init__(self, com_port):
        log.debug("%s setup", self.__class__.__name__)

        self.mimic_delay = 1.0

    def getStatus(self):
        time.sleep(self.mimic_delay)
        return "idle"

class RefArmControl(object):
    """ Communicate over a virtual com port on windows, send commands to
    control the pathlength, and polarization motors.
    """
    def __init__(self, com_port):
        log.debug("%s setup", self.__class__.__name__)

        self.com_port = com_port

        self.serial_port = serial.Serial()
        self.serial_port.baudrate = 9600
        self.serial_port.port = self.com_port
        self.serial_port.timeout = 1
        self.serial_port.writeTimeout = 1

        try:
            result = self.serial_port.close() # yes, close before open
            result = self.serial_port.open()
        except Exception as exc:
            log.critical("Problem close/open: %s", exc)
            raise exc

    def get_version(self):
        result = self.write_command("ver", 11)
        return result

    def write_command(self, command, read_bytes=24):
        """ append required control characters to the specified command,
        write to the device over the serial port, and expect the number
        of bytes returned.
        """

        result = None
        try:
            fin_command = command + '\r\n'
            log.debug("send command [%s]", fin_command)
            result = self.serial_port.write(str(fin_command))
            self.serial_port.flush()
        except Exception as exc:
            log.critical("Problem writing to port: %s", exc)
            return result

        try:
            result = self.serial_port.read(read_bytes)
            log.debug("Serial read result [%r]" % result)

        except Exception as exc:
            log.critical("Problem reading from port: %s", exc)
            return result

        log.debug("command write/read successful")
        return result

    def hwl_home(self):
        result = self.write_command("mgh h", 3)
        return result

    def hwl_relative(self, steps=90):
        result = self.write_command("mgr h %s" % steps, 3)
        return result

    def qwl_home(self):
        result = self.write_command("mgh q", 3)
        return result

    def qwl_relative(self, steps=90):
        result = self.write_command("mgr q %s" % steps, 3)
        return result
