class BowlingCard:

    def __init__(self, card):

        self.card = card
        self.frames = []
        self.score = 0
        self.last_num=0

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

        return len(self.frames) == 10

    def frameScore(self, frame):

        STRIKE = 10
        frame_score = 0

        for i in frame:
            
            if i == "X":

                frame_score += STRIKE

            elif i == "/":

                frame_score -= self.last_num
                frame_score += STRIKE

            elif i == "-":

                pass

            elif i.isdigit():

                frame_score += int(i)
                self.last_num = int(i)

        return frame_score

    def spareBonusScore(self, frame):

        return self.frameScore(frame[0])

    def strikeBonusScore(self, frames):

        rolls = 0
        strikeBonus = 0

        for frame in frames:

            for roll in frame:

                rolls += 1

                strikeBonus += self.frameScore(roll)
            
                if rolls == 2:

                    return strikeBonus


    def countTotalScore(self):

        actual_frame = -1

        for frame in self.frames:

            actual_frame += 1

            if frame[-1] == "/":

                self.score += self.frameScore(frame)
                self.score += self.spareBonusScore(self.frames[actual_frame+1])
                continue

            if frame == "X":

                self.score += self.frameScore(frame)
                self.score += self.strikeBonusScore(self.frames[actual_frame+1:actual_frame+3])
                continue

            else:

                self.score += self.frameScore(frame)


if __name__ == '__main__':

    cardStrikes = BowlingCard('9/9-9/9-12X9/9---XX-')
    cardStrikes.splitFrames()
    cardStrikes.countTotalScore()

    assert cardStrikes.score == 127