PRACTICAL 9 — CLIENT/SERVER SOCKET PROGRAM
Requires JDK (javac and java).
Open a terminal in this folder:
    javac Server.java Client.java
Terminal 1:
    java Server
Terminal 2:
    java Client
Type messages. Type BYE to close the client session.

Important accuracy note: the journal labels this practical SSL/TLS, but its supplied Java
code uses a plain Socket/ServerSocket on localhost:8081 and does not establish TLS or use
certificates. These files make the journal's client/server socket demonstration runnable;
they are not an SSL/TLS implementation.
