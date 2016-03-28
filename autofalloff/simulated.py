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
