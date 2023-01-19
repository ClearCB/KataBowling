from src.Roll import *
import pytest

@pytest.fixture
def roll():

    test_roll_num = Roll("2")
    test_roll_strike = Roll("/")
    test_roll_spare = Roll("X")

    
    return test_roll_num, test_roll_strike, test_roll_spare

@pytest.mark.test_constructor
def test_constructor(roll):

    assert roll[0].roll == "2"
    assert roll[1].roll == "/"
    assert roll[2].roll == "X"

@pytest.mark.test_rollScore
def test_rollScore(roll):

    roll[0].rollScore()
    roll[1].rollScore()
    roll[2].rollScore()

    assert roll[0].roll_score == 2
    assert roll[1].roll_score == 10
    assert roll[2].roll_score == 10