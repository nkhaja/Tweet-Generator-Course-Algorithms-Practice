from histograms import Dictogram
from probabilityModel import StochasticSample
import refinedCorpus

def main():
    txt = open("/Users/Nabil/Desktop/GoT.txt")
    cleanText = refinedCorpus.refineText(txt)
    histogram = Dictogram(cleanText)
    stochasticSampler = StochasticSample(histogram)

    return stochasticSampler.generateSentence()

