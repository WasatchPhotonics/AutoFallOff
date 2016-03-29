""" Application level controller for demonstration program. Handles data model
and UI updates with MVC style architecture.
"""

from PySide import QtCore

from . import views, devices
from . import zaber_control, oct_hardware, simulated

import logging
log = logging.getLogger(__name__)

REFARM_COMPORT = "COM3"
ZABERS_COMPORT = "COM4"

class Controller(object):
    def __init__(self, log_queue, hardware="real"):
        log.debug("Control startup")

        self.hardware = hardware

        self.form = views.BasicWindow()

        self.create_signals()
        self.bind_view_signals()

        self.setup_main_event_loop()

        self.setup_hardware(self.hardware)

    def setup_hardware(self, hardware):
        """ Create connections to physical or simulated hardware devices.
        """
        if hardware == "real":
            self.refarm = oct_hardware.RefArmControl(REFARM_COMPORT)
            self.zaber = zaber_control.ZaberControl(ZABERS_COMPORT)
        else:
            self.refarm = simulated.RefArmControl(REFARM_COMPORT)
            self.zaber = simulated.ZaberControl(ZABERS_COMPORT)

    def create_signals(self):
        """ Create signals for access by parent process.
        """
        class ControlClose(QtCore.QObject):
            exit = QtCore.Signal(str)

        self.control_exit_signal = ControlClose()

        class ControlSignals(QtCore.QObject):
            initialize = QtCore.Signal(str)
            source_paddle_move = QtCore.Signal(str)
            reference_paddle_move = QtCore.Signal(str)
            stage_move = QtCore.Signal(str)

            paddle_controller = QtCore.Signal(str)
            camera_controller = QtCore.Signal(str)
            stage_controller = QtCore.Signal(str)

        self.control_signals = ControlSignals()

    def bind_view_signals(self):
        """ Connect GUI form signals to control events.
        """
        self.form.exit_signal.exit.connect(self.close)

        self.form.ui.buttonInitialize.clicked.connect(self.initialize)
        self.form.ui.buttonStart.clicked.connect(self.start)
        self.form.ui.buttonStop.clicked.connect(self.stop)

        self.control_signals.paddle_controller.connect(self.paddle_control_update)
        self.control_signals.stage_controller.connect(self.stage_control_update)
        self.control_signals.camera_controller.connect(self.camera_control_update)

        self.control_signals.source_paddle_move.connect(self.move_source_paddle)
        self.control_signals.reference_paddle_move.connect(self.move_reference_paddle)
        self.control_signals.stage_move.connect(self.move_stage)

    def paddle_control_update(self, status):
        """ Update the paddle visualization interface to show current controller
        status.
        """
        log.info("paddle control update: %s", status)
        self.form.ui.labelPaddleController.setText(status)

    def stage_control_update(self, status):
        """ Update the stage visualization interface to show current controller
        status.
        """
        log.info("stage control update: %s", status)
        self.form.ui.labelStageController.setText(status)

    def camera_control_update(self, status):
        """ Update the camera visualization interface to show current controller
        status.
        """
        log.info("camera control update: %s", status)
        self.form.ui.labelCameraController.setText(status)

    def move_source_paddle(self, position):
        """ Update the visualization interface to show the current source paddle
        position.
        """
        log.info("Move source paddle to: %s", position)
        self.form.ui.labelSourcePaddle.setText(position)

    def move_reference_paddle(self, position):
        """ Update the visualization interface to show the current reference paddle
        position.
        """
        log.info("Move reference paddle to: %s", position)
        self.form.ui.labelReferencePaddle.setText(position)

    def move_stage(self, position):
        """ Update the visualization interface to show the current zaber
        stage position.
        """
        log.info("Move stage to: %s", position)
        self.form.ui.labelStagePosition.setText(position)


    def initialize(self):
        """ Trigger hardware initialization procedures.
        """
        log.info("Initialize flow")
        self.form.ui.labelStatus.setText("Initializing")

        self.control_signals.initialize.emit("Initializing")

        self.com_timer = QtCore.QTimer()
        self.com_timer.setSingleShot(True)
        self.com_timer.timeout.connect(self.connect_COMPORT)
        self.com_timer.start(100)
        log.debug("Post initialize")

    def connect_COMPORT(self):
        """ Attempt communication with the reference arm and zaber com port,
        report the status in the logging area.  """

        status = self.refarm.get_version()
        log.info("Reference arm version: %s", status)

        zstatus = self.zaber.getStatus()
        log.info("Zaber status: %s", zstatus)

        if zstatus == "idle" and status == "Ver:1.5I\r\nA":
            self.form.ui.labelStatus.setText("Initialized OK")

            self.control_signals.source_paddle_move.emit("Home")
            self.control_signals.reference_paddle_move.emit("Home")
            self.control_signals.stage_move.emit("Home")

            self.control_signals.paddle_controller.emit("Ready")
            self.control_signals.stage_controller.emit("Ready")
            self.control_signals.camera_controller.emit("Ready")

        else:
            log.warning("Cannot initialize")
            self.form.ui.labelStatus.setText("Failed")



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
        log.debug("Control level close")
        self.control_exit_signal.exit.emit("Control level close")

