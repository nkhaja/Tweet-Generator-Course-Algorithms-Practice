from histograms import Dictogram, Listogram
import random

class StochasticSample(list):
    def __init__(self, someDictogram):
        self.maxIndex = -1
        self.minSentenceSize = 5
        self.maxSentenceSize = 30
        for key, value in someDictogram.iteritems():
            self.maxIndex += value
            data = (key, self.maxIndex)
            self.append(data)

    def getRandomWord(self):
        randomIndex = random.randint(0, self[-1][1])
        for t in self:
            if randomIndex <= t[1]:
                return t[0]

    def generateSentence(self):
        numWords = random.randint(5,30)
        sentence = []
        for i in range (0,numWords):
            sentence.append(self.getRandomWord())
        return " ".join(sentence)





