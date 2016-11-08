import random
from random import shuffle
from sys import argv
import csv
import math
import time
import re



def frequency():
    #line = re.sub('[!@#$]', '', line)
    histogram = {}
    startTime = time.time()
    txt = open("/Users/Nabil/Desktop/GoT.txt")

    filteredText = txt.read().replace('\n', '')
    filteredText = filteredText.decode('utf-8').lower().encode('utf-8')
    removeCharacters = ['.','!','?','\"','',',','[',']',',' '-',"{", "}"]

    #"\\xe2\\x80\\x9",'\\xe2\\x80\\x94','\xe2\\x80\\x99','\\xe2\\x80\\x99'

    for ch in removeCharacters:
        filteredText = filteredText.replace(ch, "")
    filteredText = filteredText.decode('utf-8').lower().encode('utf-8')

    words = []
    words = filteredText.split()
    #print words

    for word in words:
        try:
            count = histogram[word]
            histogram[word] = histogram[word] + 1
        except:
            histogram[word] = 1

    print histogram




frequency()
