# import socket
import asyncio
import websockets

class Server():
    def __init__(self, address, port, chatbot):
        # Assign the client address & port
        self.IPAddress = address
        self.port = port

        # Point to the chatbot agent
        self.chatbot = chatbot

        # # Create the socket to server on startup and connect to UDP Client
        # self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # self.serverSocket.bind((self.IPAddress, self.port))

    async def handle_client(self, websocket, path):
        print(f"New connection from {websocket.remote_address}")

        try:
            async for message in websocket:
                print(f"Received message from client: {message}")
                
                # Aquí puedes procesar el mensaje como desees
                response = self.chatbot.ask(str(message))

                # Envia la respuesta de vuelta al cliente
                await websocket.send(str(response))

        except websockets.exceptions.ConnectionClosedError:
            print(f"Connection with {websocket.remote_address} closed.")

    def listen(self):
        # message, address = self.serverSocket.recvfrom(1024)  # OK someone pinged me.
        # print(f"received from client: {str(message.decode())}")
        # response = self.chatbot.ask(str(message.decode()))
        # self.serverSocket.sendto(str(response).encode(), address)

        start_server = websockets.serve(
            self.handle_client,
            self.IPAddress,
            self.port
        )

        print(f"WebSocket server listening on {self.IPAddress}:{self.port}")

        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()

    def close(self):
        if self.server:
            self.server.close()
            asyncio.get_event_loop().run_until_complete(self.server.wait_closed())
            print("WebSocket server closed.")

    
