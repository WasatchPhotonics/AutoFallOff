""" views for autofalloff. Includes basic window mainform.
"""
from PySide import QtGui, QtCore

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
        filename = "autofalloff/assets/example_data/1.tif"
        #filename = "autofalloff/assets/example_data/7.tif"

        from PIL import Image

        src = Image.open(filename)
        src.convert("L").save("test.png")

        new_src = Image.open(filename)
        print new_src.size
        print new_src.mode
        new_src.convert("RGBA").save("ltest.jpg")
        new_src.convert("I").save("i_test.png")
        new_src.convert("P").save("p_test.png")

        self.ui.labelSourceImage.setPixmap("i_test.png")
        self.ui.labelReferenceImage.setPixmap("p_test.png")

        import numpy
        import pyqtgraph as pg
        in_data = numpy.asarray(src, dtype=numpy.uint16)
        in_data = in_data.T
        pg.image(in_data)

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

