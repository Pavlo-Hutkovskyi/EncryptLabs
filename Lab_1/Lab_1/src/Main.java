import java.io.*;
import java.util.InputMismatchException;
import java.util.NoSuchElementException;
import java.util.Scanner;

public class Main {

    public static String readFromFile(String filePath) {
        StringBuilder content = new StringBuilder();

        try {
            var FA = new FileReader(filePath);
            Scanner in = new Scanner(FA);
            content.append(in.next());
            in.close();
        } catch (FileNotFoundException ex) {
            System.out.println("Файл не створено!");
            return "";
        } catch (InputMismatchException ex){
            System.out.println("Перевірте запис в файлі!");
            return "";
        } catch (NoSuchElementException ex) {
            System.out.println("У файлі не достатньо елементів!");
            return "";
        }
        return content.toString();
    }

    public static void writeToFile(String filePath, String str) {
        try (PrintWriter out = new PrintWriter(filePath)) {
            out.println(str);
        } catch (IOException ex) {
            System.out.println(ex.getMessage());
        }
    }

    public static void main(String[] args){
        var N = 25;
        var ukrainianStr = "ЛьвівєдинанаУкраїнімістоуякомузбереглисяархітектурніспорудичасівРенесансуНайбільшяскравимиприкладамицьогостилюслужатьцеркваУспінняікаплицяТрьохСвятихтакожкількаіншихбудинків";
        var englishStr = "Lviv is the historical capital of Galicia and Western Ukraine. It is a big cultural, political and religious centre of Ukraine. Lviv was founded in the century by Prince Danylo Romanovych";
        writeToFile("encrypt.txt", ShiftCipher.encrypt(englishStr, N));
        var decipherStr = ShiftCipher.decipher(readFromFile("encrypt.txt"), N);
        System.out.println(decipherStr);
        writeToFile("decipher.txt", decipherStr);
    }
}