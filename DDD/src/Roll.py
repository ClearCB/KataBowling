class Roll:

    def __init__(self, roll):

        self.roll = roll
        self.symbols = '-123456789'
        self.roll_score = 0

    def setScore(self, score):

        self.roll_score += score

    def getScore(self):

        return self.roll_score

    def rollScore(self):

        roll_value = self.symbols.find(self.roll)

        if roll_value != -1:

            self.setScore(roll_value)
        
        else:

            self.setScore(10)