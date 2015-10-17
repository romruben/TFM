__author__ = 'ruben'


def countWords(wordlist):
    word_table = {}
    for word in wordlist:
        count = wordlist.count(word)
        word_table[word] = count


def countWords2(wordlist):  # as proposed by Peter Otten
    word_table = {}
    for word in wordlist:
        if word in word_table:
            word_table[word] += 1
        else:
            word_table[word] = 1
        count = wordlist.count(word)
        word_table[word] = count
    return sorted(
        word_table.items(), key=lambda item: item[1], reverse=True
    )


def getWords(filename):
    with open(filename, 'r') as f:
        words = f.read().split()
    return words


def writeTable(filename, table):
    with open(filename, 'w') as f:
        for word, count in table:
            f.write("%s\t%s\n" % (word, count))


files = ['/Users/ruben/Desktop/_test/contrato.txt', '/Users/ruben/Desktop/_test/extractocuenta.txt',
         '/Users/ruben/Desktop/_test/registromercantil.txt']

words = getWords(files[2])
table = countWords2(words)
writeTable('stopwords3.txt', table)
