import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Main {
    public static void printResults(Process process) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
        String line = "";
        while ((line = reader.readLine()) != null) {
            System.out.println(line);
        }
    }

    public static void main(String[] args) throws IOException, InterruptedException {
        Scanner userInput = new Scanner(System.in);
        String pythonPath = userInput.nextLine();

        File path = new File(pythonPath);
        if (path.exists() || pythonPath.toLowerCase().equals("python")) {
            Runtime rt = Runtime.getRuntime();
            Process pr = rt.exec(pythonPath + " -m timeit -r 10");
            int count = 1;
            while (pr.isAlive()) {
                Thread.sleep(1000);
                System.out.println("Seconds from start: " + count);
                count++;
            }
            printResults(pr);
        }
        else {
            System.out.println("Error: python path is not valid.");
        }
    }
}
