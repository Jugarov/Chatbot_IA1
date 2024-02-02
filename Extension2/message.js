
function createMessage(messageType,message=null) {
    var messageBox = document.createElement('div');
    var message= document.createElement('p');
    messageBox.appendChild(message);

    if (messageType=="self"){
        messageBox.className = "ext-self-message";
        message.innerHTML = document.getElementById("chat_input").value;
        document.querySelector(".ext-message").appendChild(messageBox)

    }else if (messageType=="other"){
        messageBox.className = "ext-other-message";
        message.innerHTML =message;
        document.querySelector(".ext-message").appendChild(messageBox)
    }

    
    
}