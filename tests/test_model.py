""" Basic data model definition tests.
"""

import pytest

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

    #def test_acquisition_object_has_timestamp(self):
#
