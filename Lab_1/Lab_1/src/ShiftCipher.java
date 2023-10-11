import java.util.stream.IntStream;

public class ShiftCipher {
    private static final char[][] UKRAINIAN_ALPHABET = {
            {'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Є', 'Ж', 'З', 'И', 'І', 'Ї', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ь', 'Ю', 'Я'},
            {'а', 'б', 'в', 'г', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я'}
    };
    private static final char[][] ENGLISH_ALPHABET = {
            {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'},
            {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'},
            {' ', ',', '.', ';', ':', '!', '?', '(', ')', '[', ']', '\'', '\"', '-'}
    };

    public static String encrypt(String stringToEncrypt, int bias) {
        return moveTo(stringToEncrypt, bias);
    }

    public static String decipher(String stringToEncrypt, int bias) {
        return moveTo(stringToEncrypt, -bias);
    }

    public static String moveTo(String stringToEncrypt, int bias) {
        var encryptString = new StringBuilder();
        var isUkraineAlphabet = Character.UnicodeBlock.of(stringToEncrypt.charAt(0)) == Character.UnicodeBlock.CYRILLIC;

        for (int i = 0; i < stringToEncrypt.length(); i++)
            encryptString.append(encryptChar(stringToEncrypt.charAt(i), bias, isUkraineAlphabet));

        return encryptString.toString();
    }

    private static char encryptChar(char charToEncrypt, int bias, boolean isUkraineAlphabet) {
        var alphabet = isUkraineAlphabet ? UKRAINIAN_ALPHABET : ENGLISH_ALPHABET;
        var alph = !Character.isLetter(charToEncrypt) ? alphabet[2] : Character.isUpperCase(charToEncrypt) ? alphabet[0] : alphabet [1];
        var position = IntStream.range(0, alph.length)
                    .filter(i -> alph[i] == charToEncrypt)
                    .findFirst()
                    .orElse(-1);
        var delta = ((bias > 0 && position + Math.abs(bias) < alph.length) || (bias < 0 && position >= Math.abs(bias)))
                ? position + bias
                : position - (bias / Math.abs(bias)) * alph.length + bias;

        return alph[delta];
    }
}
