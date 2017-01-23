from histograms import Dictogram
from probabilityModel import StochasticSample
import markov_model

def main():
    textFile = open('sanitized_aristotle.txt', 'r').read()
    model = markov_model.build_markov(textFile)
    return markov_model.markov_walk(model)

if __name__ == "__main__":
    print main()
