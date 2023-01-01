class BowlingCard:

    def __init__(self, card):

        self.card = card
        self.frames = []
        self.score = 0

    def splitFrames(self):

        frame = 0
        roll = 0
        frame_to_append = ""
        index = -1

        for i in self.card:

            index += 1
            frame_to_append += i
            roll += 1

            if i == "X":

                self.frames.append(i)
                frame_to_append = ""
                frame += 1
                roll = 0

            if roll == 2:

                self.frames.append(frame_to_append)
                frame_to_append = ""
                frame += 1
                roll = 0

            if frame == 9:

                self.frames.append(self.card[index+1:])
                break

    def framesAreSplit(self):

        TEN = 10
        return len(self.frames) == TEN

    def countTotalScore(self):

        self.score = 300

if __name__ == '__main__':

    
    card = BowlingCard("12345123451234512345")
    
    card.card='9-9-9-9-9-9-9-9-9-9-'
    card.splitFrames()

    assert card.frames == ["9-","9-","9-","9-","9-","9-","9-","9-","9-","9-"]