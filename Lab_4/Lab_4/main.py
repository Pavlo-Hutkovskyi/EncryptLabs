import random


def writeToFile(line, fileName):
    with open(fileName + '.txt', "w") as file:
        file.write(line)
        file.close()


def generateGamma(str, size):
    if len(str) > size:
        return str[0:size]
    else:
        return str + generateGamma(str, size - len(str))


def generateReshuffle(array):
    random.shuffle(array)


def gammaEncrypt(string_for_encrypt, gamma, alphabet):
    return moveTo(string_for_encrypt, gamma, alphabet, 1)


def gammaDecrypt(encrypt_string, gamma, alphabet):
    return moveTo(encrypt_string, gamma, alphabet, -1)


def moveTo(string, gamma, alphabet, action):
    output_string = ''
    length_of_string = len(string)
    gamma = generateGamma(gamma, length_of_string)
    for i in range(length_of_string):
        summa = (alphabet.index(string[i].lower()) + action * alphabet.index(gamma[i].lower())) % len(alphabet)
        output_string += alphabet[summa]
    return output_string


ukrainian_alphabet = ["а", "б", "в", "г", "ґ", "д", "е", "є", "ж", "з", "и", "і", "ї", "й", "к", "л", "м", "н",
                      "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ь", "ю", "я"]
text = "ЛьвівцемістоякерозташованеназаходіУкраїниславитьсясвоєювеликоюісторієючарівною" \
       "архітектуроювеликимкультурнимспадкомтанеймовірноюгостинністюсвоїхмешканців"
gamma = "футбол"

generateReshuffle(ukrainian_alphabet)
writeToFile(text, 'text')
encrypt_string = gammaEncrypt(text, gamma, ukrainian_alphabet)
writeToFile(encrypt_string, 'encrypt')
decrypt_string = gammaDecrypt(encrypt_string, gamma, ukrainian_alphabet)
print(decrypt_string)
