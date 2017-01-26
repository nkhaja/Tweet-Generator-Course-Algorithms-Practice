from histograms import Dictogram
from probabilityModel import StochasticSample

#Each tuple maps to a dictogram with words that potentially follow
def build_markov(words):
    model = {}
    queue = []
    words = words.split()
    for index, word in enumerate(words):
        if word == '**start**':
            queue.append(word)
            queue.append(word)
            queue.append(word)
            continue

        currentPair = tuple(queue)
        if model.get(currentPair):
            model[currentPair].update([word])
        else:
            model[currentPair] = Dictogram([word])

        if word != '**end**':

            queue.pop(0)
            queue.append(word)
        else:
            queue = []

    return model


def markov_walk(markov_model):
    start = '**start**'
    end = '**end**'
    queue = [start, start, start]
    output = []
    randWord = queue[1]

    while randWord != end:
        key = tuple(queue)
        thisDictogram = markov_model[key]
        sampler = StochasticSample(thisDictogram)
        randWord = sampler.getRandomWord()
        output.append(randWord)
        queue.pop(0)
        queue.append(randWord)

    output.pop()

    if len(output) > 0:
        output[0] = output[0].capitalize()

    fullSentence = ' '.join(output)
    fullSentence += '.'

    if len(fullSentence) < 2:
        markov_walk(markov_model)
    else:
        return fullSentence

if __name__ == '__main__':
    textFile = open('sanitized_aristotle.txt', 'r').read()
    model = build_markov(textFile)
    print markov_walk(model)
