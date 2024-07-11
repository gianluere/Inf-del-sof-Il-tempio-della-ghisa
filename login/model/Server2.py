import sqlite3
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 64000))
server.listen()
print("avviato")

while True:

    (clientConnection, clientAddress) = server.accept()
    print("connesso con %s", clientConnection)

    user = clientConnection.recv(1024).decode()
    print(user)

    passw = clientConnection.recv(1024).decode()
    print(passw)

    conn = sqlite3.connect(("dati.db"))
    cur = conn.cursor()

    cur.execute("SELECT * FROM dati WHERE username = ? AND password = ?", (user, passw))

    if cur.fetchall():
        print(cur.fetchall())
        clientConnection.send("Login successful".encode())
    else:
        clientConnection.send("Login failed".encode())

    print("Inviato e fatto, riattendo")
    clientConnection.close()