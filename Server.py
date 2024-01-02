from Chatbot import Chatbot
import socket

class Server():
    def __init__(self, address, port, chatbot):
        # Assign the client address & port
        self.IPAddress = address
        self.port = port

        # Point to the chatbot agent
        self.chatbot = chatbot

        # Create the socket to server on startup and connect to UDP Client
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.serverSocket.bind((self.IPAddress, self.port))

    def listen(self):
        message, address = self.serverSocket.recvfrom(1024)  # OK someone pinged me.
        print(f"received from client: {str(message.decode())}")
        response = self.chatbot.ask(str(message.decode()))
        self.serverSocket.sendto(str(response).encode(), address)

    def close(self):
        self.serverSocket.close()

    
