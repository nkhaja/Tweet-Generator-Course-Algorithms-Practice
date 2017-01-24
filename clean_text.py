
import re
import codecs

# aristotleReg = re.compile(r'BOOK|[0-9]|(\s[IVX]\s)*|\([0-9]\)|\([A-z]\)|[;:\(\)]|--+|(\.\.)')
aristotleReg = re.compile('[0-9]')
sentenceReg = re.compile("[\?\!]|(\.\s)|(e\.g)|(i\.e)")

rumiReg = 'rumi.txt'
aristotle = 'aristotle2.txt'

def read_file(fileName):
    textFile = open(fileName, 'r').read()
    return textFile

def remove_chars(text):
     special_chars = ',-"*@#%^();\:'
     textCharsRemoved = text
     for char in special_chars:
         textCharsRemoved = textCharsRemoved.replace(char,' ')
     return textCharsRemoved

def split_sentences(textCharsRemoved):
    #identity marker for end of sentence, used in markov model
    start = '**start'
    end = ' **end** ' # extra space deliberate
    allSentences = []
    currentSentence = []

    #Replace periods with **end** marker
    endJection = sentenceReg.sub(end, textCharsRemoved)
    remove_nums = aristotleReg.sub('', endJection)

    for word in remove_nums.split():
        if word == '**end**': #whiteSpace gets removed
            currentSentence.insert(0,'**start**')
            currentSentence.append(end)
            allSentences.append(currentSentence)
            currentSentence = []
        else:
            currentSentence.append(word.lower())

    return allSentences


def write_clean(sentences):
    new_file = open('sanitized_aristotle.txt', 'w')
    for sentence in sentences:
        new_file.write(' '.join(sentence))
        new_file.write('\n')

if __name__ == '__main__':
    text = read_file('aristotle2.txt')
    cleanText = remove_chars(text)
    sentences = split_sentences(cleanText)
    write_clean(sentences)
