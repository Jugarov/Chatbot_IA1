
function createMessage(messageType) {
    var messageBox = document.createElement('div');
    var message= document.createElement('p');
    messageBox.appendChild(message);

    if (messageType=="self"){
        messageBox.className = "ext-self-message";
        message.innerHTML = document.getElementById("chat_input").value;
        document.querySelector(".ext-message").appendChild(messageBox)

    }else{
        messageBox.className = "ext-other-message";
    }

    
    
}