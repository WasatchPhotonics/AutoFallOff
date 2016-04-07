""" Controller tests that show the linkage between the data model, view, and
logging components.
Mimic the contents of the scripts/AutoFallOff.py setup section. Create the logger
with the queue handler as part of the test case, as opposed to having the
controller create the top level logger
"""

import time

import pytest

from PySide import QtTest, QtCore

from autofalloff import control
from autofalloff import applog


class TestControl:

    def test_control_logs_visible_to_caplog(self, caplog, qtbot):
        main_logger = applog.MainLogger()

        app_control = control.Controller(main_logger.log_queue)
        qtbot.wait(1000)

        app_control.close()
        time.sleep(1)

        main_logger.close()
        time.sleep(1)
        assert "Control startup" in caplog.text()
        applog.explicit_log_close()


    def test_view_logs_visible_to_caplog(self, caplog, qtbot):
        main_logger = applog.MainLogger()

        app_control = control.Controller(main_logger.log_queue)
        qtbot.wait(1000)

        app_control.close()
        time.sleep(1)

        main_logger.close()
        time.sleep(1)
        assert "Init of BasicWindow" in caplog.text()
        applog.explicit_log_close()

    def test_close_view_emits_control_signal(self, caplog, qtbot):
        """ Control script emits an event on a close condition to be processsed
        by the parent qt application, in this case qtbot. In the scripts file,
        it's the Qapplication.
        """
        main_logger = applog.MainLogger()
        app_control = control.Controller(main_logger.log_queue)

        QtTest.QTest.qWaitForWindowShown(app_control.form)

        signal = app_control.control_exit_signal.exit
        with qtbot.wait_signal(signal, timeout=1):
            app_control.form.close()

        main_logger.close()
        time.sleep(1)
        assert "Control level close" in caplog.text()
        applog.explicit_log_close()

    @pytest.fixture(scope="function")
    def basic_window(self, qtbot, request, hardware=None):
        """ Setup the controller the same way the scripts/Application
        does at every test. Ensure that the teardown is in place
        regardless of test result.
        """
        main_logger = applog.MainLogger()

        app_control = control.Controller(main_logger.log_queue,
                                         hardware=hardware)

        qtbot.addWidget(app_control.form)

        def control_close():
            app_control.close()
            main_logger.close()
            applog.explicit_log_close()

        request.addfinalizer(control_close)

        return app_control

    @pytest.fixture(scope="function")
    def control_window(self, qtbot, request):
        """ Like basic window above, but specify the controlling code to
        simulate actual delays and processing results.  """
        return self.basic_window(qtbot, request, hardware="simulated")


    def test_controller_sees_deafult_state_on_startup(self, basic_window,
                                                      qtbot, caplog):

        QtTest.QTest.qWaitForWindowShown(basic_window.form)
        assert basic_window.form.ui.labelStatus.text() == "Pre-initialization"

        qtbot.wait(1000)

    def test_controller_initialize_button_emits_signal(self, basic_window, qtbot,
                                                       caplog):
        """ Rapid iteration of signals and interface linkages tests.
        """
        qtbot.mouseClick(basic_window.form.ui.buttonInitialize, QtCore.Qt.LeftButton)
        assert "Initialize flow" in caplog.text()
        assert basic_window.form.ui.labelStatus.text() == "Initializing"

        qtbot.mouseClick(basic_window.form.ui.buttonStart, QtCore.Qt.LeftButton)
        assert "Starting" in caplog.text()
        assert basic_window.form.ui.labelStatus.text() == "Starting"

        qtbot.mouseClick(basic_window.form.ui.buttonStop, QtCore.Qt.LeftButton)
        assert "Stopping" in caplog.text()
        assert basic_window.form.ui.labelStatus.text() == "Stopping"
        qtbot.wait(3000)

    def test_click_initialize_emits_signal(self, control_window, caplog, qtbot):

        signal = control_window.control_signals.initialize
        with qtbot.wait_signal(signal, timeout=1000, raising=True):
            qtbot.mouseClick(control_window.form.ui.buttonInitialize,
                             QtCore.Qt.LeftButton)

        # after the signal is emitted, the status should be initializing
        assert control_window.form.ui.labelStatus.text() == "Initializing"
        qtbot.wait(3000)

    def test_click_initialize_triggers_all_signals(self, control_window, qtbot):
        cwcs = control_window.control_signals
        signals = [cwcs.source_paddle_move,
                   cwcs.reference_paddle_move,
                   cwcs.stage_move,
                   cwcs.paddle_controller,
                   cwcs.camera_controller,
                   cwcs.stage_controller,
                  ]

        # You'd think you could do wait_signals, alas it reports a typerror when
        # emitting signals. You can wait for each individually though
        blockers = []
        for item in signals:
            blockers.append(qtbot.waitSignal(item, timeout=1000, raising=True))

        qtbot.mouseClick(control_window.form.ui.buttonInitialize,
                         QtCore.Qt.LeftButton)
        qtbot.wait(2000) # Give the simulation time

        for item in blockers:
            print "Wait for item: ", item
            item.wait()

        qtbot.wait(2000) # Give the simulation time

    def test_click_initialize_updates_paddle_status(self, control_window, caplog, qtbot):
        signal = control_window.control_signals.source_paddle_move
        with qtbot.wait_signal(signal, timeout=1000, raising=True):
            qtbot.mouseClick(control_window.form.ui.buttonInitialize,
                             QtCore.Qt.LeftButton)

        qtbot.wait(2000) # Give the simulation time

        assert control_window.form.ui.labelSourcePaddle.text() == "Home"
        assert control_window.form.ui.labelReferencePaddle.text() == "Home"
        assert control_window.form.ui.labelStagePosition.text() == "Home"
        qtbot.wait(3000)

    def test_click_initialize_updates_controller_status(self, control_window, qtbot):
        signal = control_window.control_signals.source_paddle_move
        with qtbot.wait_signal(signal, timeout=1000, raising=True):
            qtbot.mouseClick(control_window.form.ui.buttonInitialize,
                             QtCore.Qt.LeftButton)

        qtbot.wait(2000) # Give the simulation time

        assert control_window.form.ui.labelPaddleController.text() == "Ready"
        assert control_window.form.ui.labelStageController.text() == "Ready"
        assert control_window.form.ui.labelCameraController.text() == "Ready"
        qtbot.wait(3000)

    def test_click_start_emits_signal(self, control_window, qtbot):

        signal = control_window.control_signals.start
        with qtbot.wait_signal(signal, timeout=1000, raising=True):
            qtbot.mouseClick(control_window.form.ui.buttonStart,
                             QtCore.Qt.LeftButton)
        qtbot.wait(3000)

    def test_control_creates_exam_structure(self, control_window):
        assert control_window.exam != None

        # Three acquisitions at each of the 15 stage positions
        assert len(control_window.exam) == 45

    def test_click_start_puts_first_exam_entry_in_log_file(self, control_window, qtbot, caplog):

        signal = control_window.control_signals.start
        with qtbot.wait_signal(signal, timeout=1000, raising=True):
            qtbot.mouseClick(control_window.form.ui.buttonStart,
                             QtCore.Qt.LeftButton)
        qtbot.wait(1000)
        log_str = "Acquisition 1, Reference: open, Source: home, " \
                  + "Stage: 0.1, Filename: 0.1.tif"

        assert log_str in caplog.text()

        textlog = control_window.form.ui.textLog.toPlainText()
        assert log_str in textlog


    def test_click_start_puts_last_exam_entry_in_log_file(self, control_window, qtbot, caplog):
        signal = control_window.control_signals.start
        with qtbot.wait_signal(signal, timeout=1000, raising=True):
            qtbot.mouseClick(control_window.form.ui.buttonStart,
                             QtCore.Qt.LeftButton)
        qtbot.wait(3000)
        log_str = "Acquisition 1, Reference: open, Source: home, " \
                  + "Stage: 0.1, Filename: 0.1.tif"

        assert log_str in caplog.text()

        log_str = "Acquisition 45, Reference: open, Source: open, " \
                  + "Stage: 7.0, Filename: 7.0.tif"

        assert log_str in caplog.text()

        textlog = control_window.form.ui.textLog.toPlainText()
        assert log_str in textlog

    def test_click_start_updates_reference_graph(self, control_window, qtbot):
        orig_data = control_window.form.ui.imview_reference.getProcessedImage()[0]

        signal = control_window.control_signals.start
        with qtbot.wait_signal(signal, timeout=1000, raising=True):
            qtbot.mouseClick(control_window.form.ui.buttonStart,
                             QtCore.Qt.LeftButton)

        new_data = control_window.form.ui.imview_reference.getProcessedImage()[0]

        assert len(new_data) == len(orig_data)
        print "orig ", orig_data
        print "new ", new_data
        #assert new_data[0] != orig_data[0]
        #assert new_data[-1] != orig_data[-1]
