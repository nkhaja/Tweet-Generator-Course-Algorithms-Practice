from histograms import Dictogram
from probabilityModel import StochasticSample
import refinedCorpus
import timit

def main():
    txt = open("/Users/Nabil/Desktop/GoT.txt")
    cleanText = refinedCorpus.refineText(txt)
    histogram = Dictogram(cleanText)
    stochasticSampler = StochasticSample(histogram)

    return stochasticSampler.generateSentence()


if __name__ == "__main__":

    txt = open("/Users/Nabil/Desktop/GoT.txt")
    cleanText = refinedCorpus.refineText(txt)

    hundred_words       = cleanText[0:100]
    ten_thousand_words  = cleanText[0:10000]

    hundred_hgram       = Dictogram(hundred_words)
    ten_thousand_hgram  = Dictogram(ten_thousand_words)


    stmt  = "count('{}', hundred_hgram)".format(hundred_search)
    setup = "from __main__ import count, hundred_hgram"
    timer = timeit.Timer(stmt, setup=setup)

    iterations = 10000
    result = timer.timeit(number=iterations)
    print("count time for 100-word histogram: " + str(result))
