""" Data model for acquisitions and combined exams.
"""

from PySide import QtCore

import datetime

import logging
log = logging.getLogger(__name__)

class Acquisition(object):
    def __init__(self, reference_paddle_position="home",
                 source_paddle_position="home",
                 zaber_stage_position="home",
                 camera_image_filename=None):

        self.reference_paddle_position = reference_paddle_position
        self.source_paddle_position = source_paddle_position
        self.zaber_stage_position = zaber_stage_position
        self.camera_image_filename = camera_image_filename

        self.timestamp = datetime.datetime.now()
        self.directory = self.timestamp.strftime("%Y_%m_%d %H_%M_%S")
