import random


def writeToFile(line, fileName):
    with open(fileName + '.txt', "w") as file:
        file.write(line)
        file.close()


def writeTableToFile(table):
    for i in range(len(table)):
        for j in range(len(table[i])):
            with open("table.txt", "a") as file: file.write(
                f"{table[i][j]} ")
        with open("table.txt", "a") as file:
            file.write(f"\n")
    file.close()


def createTable(frequency):
    table, data = [[] for _ in range(len(frequency))], []
    for i in range(len(frequency)):
        for k in range(frequency[i]):
            while True:
                cipheredSymbol = random.randint(100, 999)
                if cipheredSymbol not in data:
                    table[i].append(cipheredSymbol)
                    data.append(cipheredSymbol)
                    break
    return table


def encrypt(textToEncrypt, table, alphabet):
    encrypt_line = ''
    for letter in textToEncrypt:
        index = alphabet.index(letter.lower())
        encrypt_line += f"{random.choice(table[index])}" + ' '
    return encrypt_line[:-1]


ukrainian_alphabet = [" ", "а", "б", "в", "г", "ґ", "д", "е", "є", "ж", "з", "и", "і", "ї", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ь", "ю", "я"]
frequency_ukrainian_letter = [14, 7, 2, 5, 2, 1, 3, 4, 1, 1, 2, 6, 4, 1, 1, 4, 3, 3, 7, 9, 3, 4, 4, 5, 3, 1, 1, 1, 2, 1, 1, 2, 1, 2]
text = "Львів це місто яке розташоване на заході України славиться своєю великою історією чарівною архітектурою великим культурним спадком та неймовірною гостинністю своїх мешканців"

writeToFile(text, 'text')
table = createTable(frequency_ukrainian_letter)
writeToFile(encrypt(text, table, ukrainian_alphabet), 'encrypt')
writeTableToFile(table)
