import refinedCorpus
import nltk
import codecs

txt = "GoT.txt"
txt_as_string = codecs.open(txt,encoding = 'utf-8')#open(filename)
txt_as_string = txt_as_string.read()
filteredText = txt_as_string.encode('ascii','ignore')

sentence = "I went to the store"
tokenizer = nltk.data.load(filteredText)
tokens = tokenizer.tokenize(filteredText)

index = 0
for i in range(200):
    print tokens[i]
