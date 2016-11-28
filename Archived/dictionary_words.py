import random
from random import shuffle
from sys import argv
import csv
import math
import time

def pickedWords(num):
    startTime = time.time()
    txt = open("/usr/share/dict/words")
    output = []
    words = txt.read().splitlines()

    with txt as word_list:
        words = word_list.read().split()
        randomIndexes = random.sample(range(0, len(words)), num)
        for i in range(0, num):
            output.append(words[randomIndexes[i]])

    print " ".join(output)
    print(time.time() - startTime)


def pickedWordsOptimum(num):
        startTime = time.time()
        txt = open("/usr/share/dict/words")
        output = []
        words = txt.read().splitlines()
        #randomIndexes = random.sample(range(0, len(words) - 1), num)
        #output = ""
        for i in range(0, num):
            randomInt = random.randint(0, len(words)-1)
            output.append(words[randomInt])
        " ".join(output)
            #output = output + " " + words[randomInt]

        print(time.time() - startTime)
            #print output

            # function to run when file is opened prior
            # rtn_lst = [lines[random.randint(0, len(lines) -1)] for index in range(num_words)]
            # rtn = ' '.join(lst)

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
        newWord = "".join(letters)
        print newWord
        if newWord in validWords:
            badWord = False
            print "Your anagram is " +  newWord
        count = count + 1
        if count == maximum:
            print("max reached")
            break

string = raw_input("Give me a word ")
# num = raw_input("Give me a number ")
# num = int(num)
#pickedWords(num)
# pickedWordsOptimum(num)
#autocomplete(string)

properAnagram(string)
