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

        return len(self.frames) == 10

    @staticmethod
    def frameScore(frame):

        STRIKE = 10
        frame_score = 0
        for i in frame:

            if i == "X":

                frame_score += STRIKE

            elif frame[-1] == "/":

                frame_score += STRIKE

            elif frame[-1] == "-":

                if frame[0].isdigit():
                    frame_score += int(frame[0])
                else:
                    return 0

            elif frame.isdigit():

                sum = 0
                for num in i:

                    sum += int(num)
                
                frame_score += sum 

        return frame_score

    def countTotalScore(self):

        actual_frame = -1
        last_frame_sum = self.frameScore(self.frames[-1])

        for frame in self.frames[:-1]:

            actual_frame += 1
            
            if frame[-1] == "/":

                self.score += self.frameScore(self.frames[actual_frame:actual_frame+2])

            if frame == "X":

                if actual_frame == 7 or actual_frame == 8:

                    self.score += last_frame_sum

                self.score += self.frameScore(self.frames[actual_frame:actual_frame+3])
            
            else:

                self.score += self.frameScore(frame)

if __name__ == '__main__':

    cardStrikes = BowlingCard("9-9-9-9-9-9-9-9-9-9-")
    cardStrikes.splitFrames()
    cardStrikes.countTotalScore()

    assert cardStrikes.score == 90