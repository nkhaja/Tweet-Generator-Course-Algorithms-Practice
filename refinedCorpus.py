def refineText(txt):
    filteredText = txt.read()
    removeCharacters = ['\n', '','.','!','?','\"', '\"',',','[',']','-',"{", "}", ';', '\t']

    for ch in removeCharacters:
        filteredText = filteredText.replace(ch, "")

    words = filteredText.split()
    return words
