def Words(symbolsCount, word):
    global length
    global outputFile
    global count
    if len(word) == length:
        if symbolsCount.count(3) == 1 and \
           symbolsCount.count(2) == 1:
            outputFile.write(word + '\n')
            count += 1
        return
    for symbol in alphabet:
        newSymbolsCount = symbolsCount.copy()
        newSymbolsCount[ord(symbol)] += 1
        if newSymbolsCount.count(3) <= 1 and \
           newSymbolsCount.count(2) <= 1:
            word += symbol
            Words(newSymbolsCount, word)
            word = word[:-1]

inputFile = open(r"input.txt", 'r')
outputFile = open(r"output.txt", 'w')

alphabet = [str(symbol) for symbol in inputFile.readline().split()]
for symbol in alphabet:
    while alphabet.count(symbol) > 1:
        alphabet.remove(symbol)
symbolsCount = [0] * (ord(max(alphabet, key=lambda symbol: ord(symbol))) + 1)
length = int(inputFile.readline())

count = 0

Words(symbolsCount, "")
outputFile.write('\n' + str(count))

inputFile.close()
outputFile.close()
