from src.card import BowlingCard
import pytest

@pytest.fixture
def card():

    card = BowlingCard("12345123451234512345")
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
    assert card.frames == ["12","34", "51", "23", "45", "12", "34", "51", "23", "45"]

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
def test_frameScore(card):


    card.frameScore("12") == 3
    card.frameScore("4-") == 4
    card.frameScore("--") == 0
    card.frameScore("4/") == 10
    card.frameScore("X") == 10
    card.frameScore("XXX") == 30
    card.frameScore("XX-") == 20
    card.frameScore("X2/") == 20
    card.frameScore("X2-") == 12

@pytest.mark.test_spareBonusScore
def test_spareBonusScore(card):

    card.spareBonusScore(["12"]) == 1
    card.spareBonusScore(["--"]) == 0
    card.spareBonusScore(["X"]) == 10

@pytest.mark.test_strikeBonuseScore
def test_strikeBonusScore(card):

    card.strikeBonusScore(["X","X"]) == 20
    card.strikeBonusScore(["X","-2"]) == 10
    card.strikeBonusScore(["X","1-"]) == 11
    card.strikeBonusScore(["24","X"]) == 6
    card.strikeBonusScore(["5/","XX"]) == 10

@pytest.mark.test_countTotalScore
def test_countTotalScore():

    new_card = BowlingCard("12345123451234512345")
    new_card.splitFrames()
    new_card.countTotalScore()

    assert new_card.score == 60

    new_card = BowlingCard("XXXXXXXXXXXX")
    new_card.splitFrames()
    new_card.countTotalScore()

    assert new_card.score == 300

    new_card = BowlingCard("9-9-9-9-9-9-9-9-9-9-")
    new_card.splitFrames()
    new_card.countTotalScore()

    assert new_card.score == 90

    new_card = BowlingCard("5/5/5/5/5/5/5/5/5/5/5")
    new_card.splitFrames()
    new_card.countTotalScore()

    assert new_card.score == 150

    new_card = BowlingCard('9/9-9/9-12X9/9---XX-')
    new_card.splitFrames()
    new_card.countTotalScore()

    assert new_card.score == 127

    new_card = BowlingCard('9-3561368153258-7181')
    new_card.splitFrames()
    new_card.countTotalScore()

    assert new_card.score == 82

    new_card = BowlingCard("81-92/X637-52X-62/X")
    new_card.splitFrames()
    new_card.countTotalScore()

    assert new_card.score == 122

    new_card = BowlingCard("X35357162-/346-X6/7")
    new_card.splitFrames()
    new_card.countTotalScore()

    assert new_card.score == 113

    new_card = BowlingCard("-----4-7-7818/6/8/81")
    new_card.splitFrames()
    new_card.countTotalScore()

    assert new_card.score == 88

    new_card = BowlingCard("9-13315-817--38-9-18")
    new_card.splitFrames()
    new_card.countTotalScore()

    assert new_card.score == 67

    new_card = BowlingCard("-814179/5/-/1--/7/5-")
    new_card.splitFrames()
    new_card.countTotalScore()

    assert new_card.score == 95