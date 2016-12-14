from HTMLParser import HTMLParser
#python 3 from html.parser import HTMLParser
import codecs
def refineText(txt):
    # h = HTMLParser()
    txt_as_string = codecs.open(txt,encoding = 'utf-8')#open(filename)
    txt_as_string = txt_as_string.read()
    filteredText = txt_as_string.encode('ascii','ignore')
    removeCharacters = ['\n', '','.','!','?','\"', '\"',',','[',']','-',"{", "}", ';', '\t']

    for ch in removeCharacters:
        filteredText = filteredText.replace(ch, "")


    words = filteredText.split()
    return words
