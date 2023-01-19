from src.Frame import *
import pytest

@pytest.fixture
def frame():

    test_frame = Frame("12")

    return test_frame