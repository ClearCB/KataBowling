from src.Game import *
import pytest

@pytest.fixture
def first_game():

    test_game = Game("123451234512345123X45")

    return test_game

@pytest.mark.test_splitFrames
def test_splitFrames(first_game):

    first_game.splitFrames()

    assert first_game.frames[0].rolls == "12"
    assert first_game.frames[1].rolls == "34"
    assert first_game.frames[9].rolls == "X45"

@pytest.mark.test_setScore
def test_setScore(first_game):

    assert first_game.score == 0

    first_game.setScore(40)

    assert first_game.score == 40
    