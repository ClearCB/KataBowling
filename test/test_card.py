from src.card import BowlingCard
import pytest

@pytest.fixture
def card():

    card = BowlingCard("12233445566778899000")
    return card

@pytest.fixture
def cardStrikes():

    card = BowlingCard("XXXXXXXXXXXX")
    return card

@pytest.mark.test_splitFrames
def test_splitFrames(cardStrikes, card):

    cardStrikes.splitFrames()

    assert cardStrikes.frames == ["X", "X", "X", "X", "X" ,"X" ,"X" ,"X" , "X", "XXX"]

    card.splitFrames()

    assert card.frames == ["12","23", "34", "45", "56", "67", "78", "89", "90", "00"]