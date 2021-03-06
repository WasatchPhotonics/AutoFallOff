""" Basic data model definition tests.
"""

import pytest
import datetime
import time

from autofalloff import model

class TestBasicAcquisition:

    def test_acquisition_object_has_components(self):
        acq = model.Acquisition()

        assert acq.reference_paddle_position == "home"
        assert acq.source_paddle_position == "home"
        assert acq.zaber_stage_position == "home"
        assert acq.camera_image_filename == None

    def test_acquisition_object_setup_assignment(self):

        acq = model.Acquisition("open", "home", "0.1", "0.1r.tif")

        assert acq.reference_paddle_position == "open"
        assert acq.source_paddle_position == "home"
        assert acq.zaber_stage_position == "0.1"
        assert acq.camera_image_filename == "0.1r.tif"

    def test_acquisition_object_has_timestamp(self):

        # Make sure timestamp is within 1 minute of now
        now = datetime.datetime.now()

        time.sleep(0.300)

        acq = model.Acquisition()

        assert now < acq.timestamp

    def test_acquisition_object_directory_is_clean_timestamp(self):

        acq = model.Acquisition()

        clean_dir = acq.timestamp.strftime("%Y_%m_%d %H_%M_%S")
        assert clean_dir == acq.directory
