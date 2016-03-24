""" From: https://pytest.org/latest/example/simple.html, add a command
line switch to run the tests that physical presence of hardware.
"""

import pytest
def pytest_addoption(parser):
    parser.addoption("--hardware", action="store_true",
        help="run tests requiring physical hardware")
