from histograms import Dictogram
from probabilityModel import StochasticSample
import refinedCorpus

def main():
    filename = "GoT.txt"
    txt = open(filename)
    cleanText = refinedCorpus.refineText(txt)
    histogram = Dictogram(cleanText)
    stochasticSampler = StochasticSample(histogram)

    return stochasticSampler.generateSentence()

