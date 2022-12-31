class BowlingCard:

    def __init__(self, card):

        self.card = card
        self.frames = []

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


if __name__ == '__main__':

    
    card = BowlingCard("12345123451234512345")
    
    card.splitFrames()

    assert card.frames == ["12","23", "34", "45", "56", "67", "78", "89", "90", "00"]