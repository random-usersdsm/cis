import java.io.*;
import java.net.*;
import java.util.Scanner;

public class Client {
    public static void main(String[] args) {
        try (Socket socket = new Socket("localhost", 8081);
             BufferedReader reader = new BufferedReader(
                 new InputStreamReader(socket.getInputStream()));
             BufferedWriter writer = new BufferedWriter(
                 new OutputStreamWriter(socket.getOutputStream()));
             Scanner scanner = new Scanner(System.in)) {

            System.out.println("Connected. Type messages; enter BYE to exit.");
            while (true) {
                System.out.print("Send message to server: ");
                String message = scanner.nextLine();
                writer.write(message);
                writer.newLine();
                writer.flush();
                System.out.println("Server: " + reader.readLine());
                if ("BYE".equalsIgnoreCase(message)) break;
            }
        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
            System.out.println("Start Server.java first in another terminal.");
        }
    }
}
