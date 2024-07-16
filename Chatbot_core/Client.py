import asyncio
import websockets

class Client():
    def __init__(self, address, port):
        # Assign the client address & port
        #self.IPAddress = address
        #self.port = port

        # Create the socket to server on startup
        #self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.uri = "wss://chatbotia1.ingenieria.uncuyo.edu.ar"

    def read(self):
        message = input("Enter message prompt from client: ")
        self.sendMessage(message)

    async def sendMessage(self, message):
        #self.clientSocket.sendto(message.encode(), (self.IPAddress, self.port))
        async with websockets.connect(self.uri) as websocket:
            # Enviar un mensaje al servidor WebSocket
            await websocket.send(str(message))
            # Esperar una respuesta del servidor
            response = await websocket.recv()
            print(f"Respuesta del servidor: {response}")

    def listen(self):
        message, address = self.clientSocket.recvfrom(1024)  # OK someone pinged me.
        print(f"Response received from server: {message.decode()}")

    def close(self):
        self.clientSocket.close()

