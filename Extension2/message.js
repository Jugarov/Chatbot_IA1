
function createMessage(messageType,message=null) {
    var messageBox = document.createElement('div');
    var message= document.createElement('p');
    messageBox.appendChild(message);

    if (messageType=="self"){
        messageBox.className = "ext-self-message";
        message.innerHTML = document.getElementById("chat_input").value;
        document.querySelector(".ext-message").appendChild(messageBox)

    }

   /* }else if (messageType=="other"){
        messageBox.className = "ext-other-message";
        message.innerHTML =message;
        document.querySelector(".ext-message").appendChild(messageBox)
    }*/
  
    resetInput();

}

document.addEventListener('keydown', function (event) {
    if (event.key === 'Enter') {
        // Llama a las funciones que se ejecutan al hacer clic en el botón
        sendMessage();
        createMessage('self');
    }
});

function resetInput() {
    document.getElementById('chat_input').value = '';
}