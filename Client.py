import socket

class Client():
    def __init__(self, address, port):
        # Assign the client address & port
        self.IPAddress = address
        self.port = port

        # Create the socket to server on startup
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def read(self):
        message = input("Enter message prompt from client: ")
        self.sendMessage(message)

    def sendMessage(self, message):
        self.clientSocket.sendto(message.encode(), (self.IPAddress, self.port))

    def listen(self):
        message, address = self.clientSocket.recvfrom(1024)  # OK someone pinged me.
        print(f"Response received from server: {message.decode()}")

    def close(self):
        self.clientSocket.close()

