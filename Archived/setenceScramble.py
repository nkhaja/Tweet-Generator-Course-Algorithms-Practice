import random
from random import shuffle
def scrambleSentence():
    sentence = raw_input("Give me words seperated by spaces ")
    words = sentence.split()
    print(words)
    randomIndexes = random.sample(range(0, len(words)), len(words))
    outArray = []

    for i in randomIndexes:
        outArray.append(words[i])

    print " ".join(outArray)

def reverseString():
    sentence = raw_input("Give me words seperated by spaces ")
    words = sentence.split()
    reverse = " ".join(reversed(words))
    print reverse

def shuffle_word(word):
    letters = list(word)
    shuffle(letters)
    print ''.join(letters)

#scrambleSentence()
#reverseString()
shuffle_word('amazing')


def newShuffle(array):
    randomIndexes = random.sample(range(0, len(words)), len(words))
    newArray = []
    count = 0
    for i in range(0,len(array)):
        newArray.append(array[i])
    return newArray
