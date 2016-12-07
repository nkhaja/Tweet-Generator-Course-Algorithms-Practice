import timeit
def make_histogram(words):
    hgram = []                           # create a new list called hgram
    for word in words:                   # for each word in the list of words
        index = find(word, hgram)        # check if word is in hgram already
        if index == None:                # if word is not in histogram
            hgram.append((word, 1))      # add a new word-count pair to hgram
        else:                            # if word is already in hgram
            count = hgram[index][1]      # find its current count
            new_pair = (word, count + 1) # make a new word-count pair
            hgram[index] = new_pair      # replace word-count pair
    return hgram


def find(item, hgram):
    for index, pair in enumerate(hgram):
        if pair[0] == item:
            return index
    return None

def list_of_words(length):
    dict_words = '/usr/share/dict/words'
    words_str  = open(dict_words, 'r').read()
    all_words  = words_str.split("\n")
    return all_words[0:length]

def count(word, hgram):
    index = find(word, hgram)
    if index:
        word_count_pair = hgram[index]
        return word_count_pair[1]
    else:
        return 0


if __name__ == "__main__":

    hundred_words       = list_of_words(100)
    ten_thousand_words  = list_of_words(10000)

    hundred_hgram       = make_histogram(hundred_words)
    ten_thousand_hgram  = make_histogram(ten_thousand_words)

    hundred_search      = hundred_words[-1]
    ten_thousand_search = ten_thousand_words[-1]

    stmt  = "count('{}', hundred_hgram)".format(hundred_search)
    setup = "from __main__ import count, hundred_hgram"
    timer = timeit.Timer(stmt, setup=setup)

    iterations = 10000
    result = timer.timeit(number=iterations)
    print("count time for 100-word histogram: " + str(result))
