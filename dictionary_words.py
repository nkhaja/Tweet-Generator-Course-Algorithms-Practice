import random
from random import shuffle
from sys import argv
import csv
import math

def pickedWords(num):
    txt = open("/usr/share/dict/words")
    output = []
    with txt as word_list:
        words = word_list.read().split()
        randomIndexes = random.sample(range(0, len(words)), len(words))
        for i in range(0, num):
            output.append(words[randomIndexes[i]])

    print " ".join(output)


def pickedWordsOptimum(num):
        txt = open("/usr/share/dict/words")
        output = []
        with txt as word_list:
            words = word_list.read().split()
            randomIndexes = random.sample(range(0, len(words)), len(words))
            output = ""
            for i in range(0, num):
                output = output + " " + words[randomIndexes[i]]

            print output

def autocomplete(string):
    txt = open("/usr/share/dict/words")
    output = []
    with txt as word_list:
        words = word_list.read().split()
        for word in words:
            if word.startswith(string):
                output.append(word)
    print output

def getDict():
    txt = open("/usr/share/dict/words")
    output = []
    with txt as word_list:
        words = word_list.read().split()
        return words

def properAnagram(string):
    validWords = getDict()
    badWord = True
    count = 0
    maximum = math.factorial(len(string))
    print maximum

    while badWord == True:
        letters = list(string)
        shuffle(letters)
        newWord = " ".join(letters)
        print newWord
        if newWord in validWords:
            badWord = False
            print newWord
        count = count + 1
        if count == maximum:
            print("max reached")
            break






string = raw_input("Give me a word ")
# num = raw_input("Give me a number ")
# num = int(num)
# pickedWords(num)
# pickedWordsOptimum(num)
#autocomplete(string)

properAnagram(string)
