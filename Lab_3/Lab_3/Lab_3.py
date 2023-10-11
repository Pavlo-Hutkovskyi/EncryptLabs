def readFromFile(fileName):
    with open(fileName, 'r') as file:
        lines = file.read()
        file.close()
    return lines


def writeToFile(line, fileName):
    with open(fileName + '.txt', "w") as file:
        file.write(line)
        file.close()


def createTable(frequency):
    table = [[] for _ in frequency]
    for i, freq in enumerate(frequency):
        table[i] = [0] * freq
    return table


def findIndex(array, number):
    for i in range(len(array)):
        if number in array[i]:
            return i
    return -1


def printFrequencyTable(arraySymbol, str):
    print("\n+===+========+")
    for symbol in arraySymbol:
        print("'{}' | {}%".format(symbol, round(str.count(symbol) / len(str) * 100, 3)))
    print("+===+========+\n")

ukrainian_alphabet = [" ", "а", "б", "в", "г", "ґ", "д", "е", "є", "ж", "з", "и", "і", "ї", "й", "к", "л", "м", "н",
                      "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ь", "ю", "я"]
frequency_ukrainian_letter = [14, 7, 2, 5, 2, 1, 3, 4, 1, 1, 2, 6, 4, 1, 1, 4, 3, 3, 7, 9, 3, 4, 4, 5, 3, 1, 1, 1, 2, 1,
                              1, 2, 1, 2]
text = "Львів це місто яке розташоване на заході України славиться своєю великою історією чарівною" \
       " архітектурою великим культурним спадком та неймовірною гостинністю своїх мешканців"

table, i = createTable(frequency_ukrainian_letter), 0
readLine = readFromFile('encrypt.txt')
numbers = readLine.split(' ')
for line in readFromFile('table.txt').splitlines():
    table[i] = line.split()
    i += 1
outputLine = ''
for number in numbers:
    outputLine += ukrainian_alphabet[findIndex(table, number)]
print(outputLine)

printFrequencyTable(ukrainian_alphabet, outputLine)
printFrequencyTable([" ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"], readLine)
