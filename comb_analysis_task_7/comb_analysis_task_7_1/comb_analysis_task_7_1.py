def BinaryCodes(word):
    global length
    global accommodationLength
    global binaryCodes
    if len(word) == length:
        binaryCodes.append(word)
        return
    for symbol in ['1', '0']:
        if (word + symbol).count('1') <= accommodationLength and \
           (word + symbol).count('0') <= length - accommodationLength:
            word += symbol
            BinaryCodes(word)
            word = word[:-1]

def Permutations(subset, word):
    global accommodationLength
    global outputFile
    global count
    if len(word) == accommodationLength:
        outputFile.write(word + '\n')
        count += 1
        return
    for symbol in subset:
        if symbol not in word:
            word += symbol
            Permutations(subset, word)
            word = word[:-1]

inputFile = open(r"input.txt", 'r')
outputFile = open(r"output.txt", 'w')

alphabet = [str(symbol) for symbol in inputFile.readline().split()]
for symbol in alphabet:
    while alphabet.count(symbol) > 1:
        alphabet.remove(symbol)
length = len(alphabet)
accommodationLength = int(inputFile.readline())

binaryCodes = []
subsets = []
count = 0

BinaryCodes("")
for word in binaryCodes:
    subset = []
    for i in range(length):
        if word[i] == '1':
            subset.append(alphabet[i])
    subsets.append(subset)
for subset in subsets:
    Permutations(subset, "")
outputFile.write('\n' + str(count))

inputFile.close()
outputFile.close()
