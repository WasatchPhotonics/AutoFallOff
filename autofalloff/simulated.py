""" Provide a bare-bones simulation interface with sleep delays to mimic
actual hardware responses.
"""

import time
import logging

log = logging.getLogger(__name__)

class RefArmControl(object):
    def __init__(self, com_port):
        log.debug("%s setup", self.__class__.__name__)

        self.version = "Ver:1.5I\r\nA"
        self.mimic_delay = 1.0

    def get_version(self):
        time.sleep(self.mimic_delay)
        return self.version

class ZaberControl(object):
    """ Provide a bare-bones simulation interface with sleep delays to mimic
    actual hardware responses.
    """
    def __init__(self, com_port):
        log.debug("%s setup", self.__class__.__name__)

        self.mimic_delay = 1.0

    def getStatus(self):
        time.sleep(self.mimic_delay)
        return "idle"

class SaperaControl(object):
    """ Provied a bare-bones simulation interface with sleep delays to mimic
    actual hardware responses. Generate tif data from saved examples.import
    """
    def __init__(self):
        log.debug("%s setup", self.__class__.__name__)

        self.mimic_delay = 1.0
        self.position = 0
        self.distances = [0.2, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]

    def get_status(self):
        time.sleep(self.mimic_delay)
        return "idle"

    def get_image(self):
        """ Cycle through the distances list, returning the next in order each
        acquisition.
        """

        directory = "autofalloff\\assets\\example_data"
        current = self.distances[self.position]
        filename = "%s\\%s.tif" % (directory, current)

        self.position += 1
        if self.position == len(self.distances):
            self.position = 0

        with open(filename, "rb") as tif_file:
            raw_data = tif_file.read()

        log.debug("File %s length %s", filename, len(raw_data))

        return raw_data


