import java.io.*;
import java.net.*;

public class Server {
    public static void main(String[] args) throws IOException {
        try (ServerSocket serverSocket = new ServerSocket(8081)) {
            System.out.println("Server listening on port 8081...");
            while (true) {
                try (Socket socket = serverSocket.accept();
                     BufferedReader reader = new BufferedReader(
                         new InputStreamReader(socket.getInputStream()));
                     BufferedWriter writer = new BufferedWriter(
                         new OutputStreamWriter(socket.getOutputStream()))) {
                    String message;
                    while ((message = reader.readLine()) != null) {
                        System.out.println("Client: " + message);
                        writer.write("Message Received");
                        writer.newLine();
                        writer.flush();
                        if ("BYE".equalsIgnoreCase(message)) break;
                    }
                } catch (IOException e) {
                    System.out.println("Client connection error: " + e.getMessage());
                }
            }
        }
    }
}
