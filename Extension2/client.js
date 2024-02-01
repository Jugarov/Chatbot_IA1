class Client {
    constructor(address, port) {
        this.address = address;
        this.port = port;
        this.socket = new WebSocket(`ws://${address}:${port}`);

        this.socket.addEventListener('open', () => {
            console.log('Connection established.');
        });

        this.socket.addEventListener('message', (event) => {
            console.log(`Response received from server: ${event.data}`);
        });

        this.socket.addEventListener('close', () => {
            console.log('Connection closed.');
        });

        this.socket.addEventListener('error', (error) => {
            console.error(`WebSocket error: ${error}`);
        });
    }

    read(message) {
        console.log("Message from textarea:", message);
        if (this.socket.readyState === WebSocket.OPEN) {
            this.sendMessage(message);
        } else {
            console.error("WebSocket not open yet.");
        }
    }

    sendMessage(message) {
        this.socket.send(message);
    }

    close() {
        this.socket.close();
    }
}

let client;

function startApp() {
    client = new Client("25.69.81.47", 2620);
}

function sendMessage() {
    const textareaValue = document.getElementById("chat_input").value;
    try {
        client.read(textareaValue);
    } catch (error) {
        console.error("ERROR:", error);
    }
}

// Llama a startApp() cuando la pÃ¡gina se carga
window.addEventListener('load', startApp);