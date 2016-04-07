""" views for autofalloff. Includes basic window mainform.
"""
from PySide import QtGui, QtCore

from PIL import Image  # for creating placeholder imagery at startup
import numpy
import pyqtgraph

from .assets import basic_layout

import logging
log = logging.getLogger(__name__)

class BasicWindow(QtGui.QMainWindow):
    """ Load the QT designer created layout based on default qt WIMP controls.
    """
    def __init__(self, title="BasicWindow", layout=basic_layout,
                 geometry=[250, 250, 1000, 700]):
        log.debug("Init of %s", self.__class__.__name__)
        super(BasicWindow, self).__init__()

        self.ui = layout.Ui_MainWindow()
        self.ui.setupUi(self)

        self.create_signals()
        # x, y, w, h
        self.setGeometry(geometry[0], geometry[1], geometry[2], geometry[3])

        self.load_placeholder_images()

        app_icon = QtGui.QIcon(":ui/images/ApplicationIcon.ico")
        self.setWindowIcon(app_icon)
        self.setWindowTitle(title)
        self.show()

    def load_placeholder_images(self):
        """ Use the example data 16 bit tiffs, make sure they can be displayed
        in the qt label. Conversion is from:
        http://blog.philippklaus.de/2011/08/handle-16bit-tiff-images-in-python/
        """
        directory = "autofalloff/assets/example_data"
        reference_filename = "%s/1r.tif" % directory
        source_filename = "%s/4s.tif" % directory
        combined_filename = "%s/7.tif" % directory

        # Open the image, convert in place
        ref_img = Image.open(reference_filename)
        ref_img.convert("L")

        # Assign it to a numpy array, transpose X and Y dimensions
        ref_data = numpy.asarray(ref_img, dtype=numpy.uint16).T

        # Create an imageview control, assign the data and make it visible
        self.ui.imview_reference = pyqtgraph.ImageView()
        self.ui.imview_reference.setImage(ref_data)
        self.ui.stackedWidgetReference.addWidget(self.ui.imview_reference)
        self.ui.stackedWidgetReference.setCurrentIndex(2)

        # source image
        src_img = Image.open(source_filename)
        src_img.convert("L")
        src_data = numpy.asarray(src_img, dtype=numpy.uint16).T

        self.ui.imview_source = pyqtgraph.ImageView()
        self.ui.imview_source.setImage(src_data)
        self.ui.stackedWidgetSource.addWidget(self.ui.imview_source)
        self.ui.stackedWidgetSource.setCurrentIndex(2)


        # Combined image
        com_img = Image.open(combined_filename)
        com_img.convert("L")
        com_data = numpy.asarray(com_img, dtype=numpy.uint16).T

        self.ui.imview_combined = pyqtgraph.ImageView()
        self.ui.imview_combined.setImage(com_data)
        self.ui.stackedWidgetCombined.addWidget(self.ui.imview_combined)
        self.ui.stackedWidgetCombined.setCurrentIndex(2)


    def create_signals(self):
        """ Create signal objects to be used by controller and internal simple
        events.
        """
        class ViewClose(QtCore.QObject):
            """ Emit a signal for control upstream.
            """
            exit = QtCore.Signal(str)

        self.exit_signal = ViewClose()

    def closeEvent(self, event):
        """ Custom signal for controller to catch when the GUI close event is
        triggered by the user.
        """
        log.debug("View level close")
        self.exit_signal.exit.emit("close event")

