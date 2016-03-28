""" Application level controller for demonstration program. Handles data model
and UI updates with MVC style architecture.
"""

from PySide import QtCore

from . import views, devices
from . import zaber_control, oct_hardware

import logging
log = logging.getLogger(__name__)

REFARM_COMPORT = "COM3"
ZABERS_COMPORT = "COM4"

class Controller(object):
    def __init__(self, log_queue):
        log.debug("Control startup")

        # Create a separate process for the qt gui event loop
        self.form = views.BasicWindow()

        self.create_signals()

        self.bind_view_signals()

        self.device = devices.LongPollingSimulateSpectra(log_queue)
        self.total_spectra = 0

        self.setup_main_event_loop()

    def create_signals(self):
        """ Create signals for access by parent process.
        """
        class ControlClose(QtCore.QObject):
            exit = QtCore.Signal(str)

        self.control_exit_signal = ControlClose()

    def bind_view_signals(self):
        """ Connect GUI form signals to control events.
        """
        self.form.exit_signal.exit.connect(self.close)

        self.form.ui.buttonInitialize.clicked.connect(self.initialize)
        self.form.ui.buttonStart.clicked.connect(self.start)
        self.form.ui.buttonStop.clicked.connect(self.stop)

    def initialize(self):
        """ Trigger hardware initialization procedures.
        """
        log.info("Initialize flow")
        self.form.ui.labelStatus.setText("Initializing")

        self.com_timer = QtCore.QTimer()
        self.com_timer.setSingleShot(True)
        self.com_timer.timeout.connect(self.connect_com_port)
        self.com_timer.start(100)
        log.debug("Post initialize")

    def connect_com_port(self):
        """ Attempt communication with the reference arm and zaber com port,
        report the status in the logging area.  """
        log.debug("1 Post initialize")
        self.refarm = oct_hardware.RefArmControl(REFARM_COMPORT)
        status = self.refarm.get_version()

        log.info("Reference arm version: %s", status)
        if status == "Ver:1.5I\r\nA":
            log.info("Reference arm version: %s", status)

        self.zaber = zaber_control.ZaberControl(ZABERS_COM_PORT)
        zstatus = self.zaber.getStatus()

        log.info("Zaber status: %s", zstatus)
        if status == "test":
            self.form.ui.labelStatus.setText("Initialized OK")



    def start(self):
        """ Start the scan procedure.
        """
        log.info("Starting")
        self.form.ui.labelStatus.setText("Starting")

    def stop(self):
        """ Stop the scan procedure.
        """
        log.info("Stopping")
        self.form.ui.labelStatus.setText("Stopping")

    def setup_main_event_loop(self):
        """ Create a timer for a continuous event loop, trigger the start.
        """
        log.debug("Setup main event loop")
        self.continue_loop = True
        self.main_timer = QtCore.QTimer()
        self.main_timer.setSingleShot(True)
        self.main_timer.timeout.connect(self.event_loop)
        #self.main_timer.start(0)

    def event_loop(self):
        """ Process queue events, interface events, then update views.
        """
        result = self.device.read()
        if result is not None:
            self.total_spectra += 1
            self.form.ui.textLog.append("%s spectra read" \
                                        % self.total_spectra)

        if self.continue_loop:
            self.main_timer.start(0)

    def close(self):
        self.continue_loop = False
        self.device.close()
        log.debug("Control level close")
        self.control_exit_signal.exit.emit("Control level close")

