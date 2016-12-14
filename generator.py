from histograms import Dictogram
from probabilityModel import StochasticSample
import refinedCorpus
import codecs
def main():
    filename = "GoT.txt"
    cleanText = refinedCorpus.refineText(filename)
    histogram = Dictogram(cleanText)
    stochasticSampler = StochasticSample(histogram)

    return stochasticSampler.generateSentence()
