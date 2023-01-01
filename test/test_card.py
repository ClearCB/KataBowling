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

@pytest.mark.test_frameScore
def test_frameScore():


    BowlingCard.frameScore("12") == 3
    BowlingCard.frameScore("4-") == 4
    BowlingCard.frameScore("--") == 0
    BowlingCard.frameScore("4/") == 10
    BowlingCard.frameScore("X") == 10
    BowlingCard.frameScore("XXX") == 30
    BowlingCard.frameScore("XX-") == 20
    BowlingCard.frameScore("X2/") == 20
    BowlingCard.frameScore("X2-") == 12


@pytest.mark.test_countTotalScore
def test_countTotalScore(card, cardStrikes):

    card.splitFrames()
    card.countTotalScore()

    assert card.score == 91

    card.card='9-9-9-9-9-9-9-9-9-9-'
    card.score = 0
    card.splitFrames()
    card.countTotalScore()

    assert card.score == 90

    card.card='12345123451234512345'
    card.score = 0
    card.splitFrames()
    card.countTotalScore()

    assert card.score == 60

    card.card='5/5/5/5/5/5/5/5/5/5/5'
    card.score = 0
    card.splitFrames()
    card.countTotalScore()

    assert card.score == 150

    cardStrikes.splitFrames()
    cardStrikes.countTotalScore()

    assert cardStrikes.score == 300