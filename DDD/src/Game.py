from src.Frame import * 



class Game:

    def __init__(self,card):
        
        self.card = card
        self.frames = []
        self.score = 0

    def setScore(self, score):

        self.score += score

    def splitFrames(self):

        index_frame = 0
        roll = 0
        frame_to_append = ""
        index = -1

        for i in self.card:

            index += 1
            frame_to_append += i
            roll += 1

            if i == "X":

                frame = Frame(i)
                self.frames.append(frame)
                frame_to_append = ""
                index_frame += 1
                roll = 0

            if roll == 2:

                frame = Frame(frame_to_append)
                self.frames.append(frame)
                frame_to_append = ""
                index_frame += 1
                roll = 0

            if index_frame == 9:

                frame = Frame(self.card[index+1:])
                self.frames.append(frame)
                break

    def totalScore(self):

        for frame in self.frames:

            self.setScore(frame.scoreFrame())