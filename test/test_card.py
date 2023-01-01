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

    card.card='9-9-9-9-9-9-9-9-9-9-'
    card.frames=[]
    card.splitFrames()

    assert card.frames == ["9-","9-","9-","9-","9-","9-","9-","9-","9-","9-"]

    card.card='9/9-9/9-12X9/9-XXX-'
    card.frames=[]
    card.splitFrames()

    assert card.frames == ["9/","9-","9/","9-","12","X","9/","9-","X","XX-"]

@pytest.mark.test_framesAreSplit
def test_framesAreSplit(card):

    assert card.framesAreSplit() == False

    card.splitFrames()

    assert card.framesAreSplit() == True


@pytest.mark.test_countTotalScore
def test_countTotalScore(card):

    card.splitFrames()
    card.countTotalScore()

    assert card.score == 300