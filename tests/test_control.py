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

    def test_device_logs_in_file_only(self, caplog, qtbot):
        """ Shows the expected behavior. Demonstrates that the capturelog
        fixture on py.test does not see sub process entries.
        """
        assert applog.delete_log_file_if_exists() == True

        main_logger = applog.MainLogger()

        app_control = control.Controller(main_logger.log_queue)
        qtbot.wait(1000)

        app_control.close()
        time.sleep(1)

        main_logger.close()
        time.sleep(1)

        log_text = applog.get_text_from_log()
        assert "SimulateSpectra setup" in log_text
        assert "SimulateSpectra setup" not in caplog.text()
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
    def basic_window(self, qtbot, request):
        """ Setup the controller the same way the scripts/Application
        does at every test. Ensure that the teardown is in place
        regardless of test result.
        """
        main_logger = applog.MainLogger()

        app_control = control.Controller(main_logger.log_queue)

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
        return self.basic_window(qtbot, request)


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

    def test_controller_simulated_logic_flow(self, control_window, qtbot, caplog):
        """ More accurate timing to reflect the actual hardware control.
        """

        qtbot.mouseClick(control_window.form.ui.buttonInitialize,
                         QtCore.Qt.LeftButton)

