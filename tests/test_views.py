""" Basic GUI tests with default qt controls for verifying functionality.
Designed to be skinned later with SVG controls like in bluegraph.
"""

import pytest

from PySide import QtCore, QtTest

from autofalloff import views

class TestBasicMainWindow:

    @pytest.fixture(scope="function")
    def basic_form(self, qtbot, request):
        """ Create the view at every setup, close it on final.
        """
        new_form = views.BasicWindow()

        def form_close():
            new_form.close()
        request.addfinalizer(form_close)

        return new_form

    def test_form_has_default_setup(self, basic_form, qtbot):
        assert basic_form.ui.labelStatus.text() == "Pre-initialization"
        assert basic_form.width() >= 1000
        assert basic_form.height() >= 700

