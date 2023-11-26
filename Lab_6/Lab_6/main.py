def readFromFileMatrix(fileName):
    matrix = []
    with open(fileName, "r", encoding="utf-8") as file:
        lines = file.readlines()
    for line in lines:
        row = list(line.strip())
        row = [char for char in row if char != ' ']
        matrix.append(row)
    return matrix


def readFromFile(fileName):
    with open(fileName, 'r', encoding="utf-8") as file:
        lines = file.read()
        file.close()
    return lines


def findInMatrix(el, table):
    for i in range(4):
        for j in range(8):
            if el == table[i][j]:
                return i, j


def decrypt(text, table):
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
            out += table[i1][-1] if j1 - 1 < 0 else table[i1][j1 - 1]
            out += table[i1][-1] if j2 - 1 < 0 else table[i1][j2 - 1]
        # По стовпцях
        elif j1 == j2:
            out += table[-1][j1] if i1 - 1 < 0 else table[i1 - 1][j1]
            out += table[-1][j1] if i2 - 1 < 0 else table[i2 - 1][j2]
    return out


line = readFromFile('text.txt')
table = readFromFileMatrix('matrix.txt')
print(line)
for i in table:
    print(i)
print(decrypt(line, table))
