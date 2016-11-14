import random
from random import shuffle
from sys import argv
import csv
import math
import time
import re


def buildHistogram():
    histogram = {}
    startTime = time.time()
    txt = open("/Users/Nabil/Desktop/GoT.txt")

    filteredText = txt.read().replace('\n', '')
    removeCharacters = ['.','!','?','\"', '\"',',','[',']','-',"{", "}", ';', '\t']
    removeCharacters

    for ch in removeCharacters:
        filteredText = filteredText.replace(ch, "")

    #words = []
    words = filteredText.split()

    for word in words:
        try:
            count = histogram[word]
            histogram[word] = histogram[word] + 1
        except:
            histogram[word] = 1
    return histogram



def buildTupleArray(histogram):
    count =  -1
    output = []
    for key, value in histogram.iteritems():
        count += value
        data = (key, count)
        output.append(data)
    return output


def getRandomWord(ta):
    #tuple(word, endIndex)

    randomIndex = random.randint(0, ta[-1][1])
    for t in ta:
        if randomIndex <= t[1]:
            return t[0]
    print ("nothing found")



def generateSentence():
    histogram = buildHistogram()
    tupleArray = buildTupleArray(histogram)
    numWords = random.randint(5,30)
    sentence = []
    for i in range (0,numWords):
        sentence.append(getRandomWord(tupleArray))
    return " ".join(sentence)


if __name__ == "__main__":
    app.run()
