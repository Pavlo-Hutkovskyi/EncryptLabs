import random
# "ґ"


def cipherTable(alphabet):
    random.shuffle(alphabet)
    return [alphabet[i:i+8] for i in range(0, len(ukrainian_alphabet), 8)]


def encrypt(text, table):
    out = ''
    for i in range(0, len(text), 2):
        two_letters = text[i:i + 2]
        i1, j1 = findInMatrix(two_letters[0], table)
        i2, j2 = findInMatrix(two_letters[1], table)
        # По прямокутнику
        if i1 != i2 and j1 != j2:
            out += table[i2][j1] + table[i1][j2]
        # По рядку
        elif i1 == i2:
            out += table[i1][0] if j1 >= len(table[0]) - 1 else table[i1][j1 + 1]
            out += table[i1][0] if j2 >= len(table[0]) - 1 else table[i1][j2 + 1]
        # По стовпцях
        elif j1 == j2:
            out += table[0][j1] if i1 >= len(table) - 1 else table[i1 + 1][j1]
            out += table[0][j1] if i2 >= len(table) - 1 else table[i2 + 1][j2]
    return out


def findInMatrix(el, table):
    for i in range(len(table)):
        for j in range(len(table[0])):
            if el == table[i][j]: return i, j


def writeToFileMatrix(table, fileName):
    with open(fileName, "w", encoding="utf-8") as file:
        for row in table:
            file.write(" ".join(map(str, row)) + "\n")


def readFromFileMatrix(fileName):
    matrix = []
    with open(fileName, "r", encoding="utf-8") as file:
        lines = file.readlines()
    for line in lines:
        row = list(line.strip())
        row = [char for char in row if char != ' ']
        matrix.append(row)
    return matrix


def writeToFile(line, fileName):
    with open(fileName + '.txt', "w", encoding='utf-8') as file:
        file.write(line)
        file.close()


ukrainian_alphabet = ["а", "б", "в", "г", "д", "е", "є", "ж", "з", "и", "і", "ї", "й", "к", "л", "м", "н",
                      "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ь", "ю", "я"]
table = readFromFileMatrix('matrix.txt')
writeToFileMatrix(table, 'matrix.txt')
for i in table:
    print(i)
str = "ЛьвівЦеМістоЯкеРозташованеНаЗаходіУкраїниСлавитьсяСвоєюВеликоюІсторієюЧарівноюАрхітектуроюВеликимКультурнимСпадкомТаНеймовірноюГостинністюСвоїхМешканців"
writeToFile(encrypt('гутковськийпавловодафутболгутк', table), 'text')
print(encrypt('гутковськийпавловодафутболгутк', table))
