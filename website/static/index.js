//Executes when DOM contents are fully loaded
document.addEventListener('DOMContentLoaded', () => {

    //Executes if the user is in the chat room page
    if (window.location.pathname == "/"){
        var socket = io.connect('http://' + document.domain + ':' + location.port); //Triggers a 'connection' event

        //On receiving a message, append it to the 'messages' div
        socket.on('messaging', data => {
            console.log("Message recieved: " + data)
            var content = `
            <div class="container" style="
            border: 2px solid #dedede;
            background-color: #f1f1f1;
            border-radius: 5px;
            padding: 10px;
            margin: 10px 0;
            animation-name: slidein;
            animation-duration: 0.5s;
            ">` + '<p>' + data + '</p>'
            var updateDiv = document.getElementById("messages");
            updateDiv.insertAdjacentHTML("beforeend", content);
            scrollSmoothToBottom("messages");
          

        });

        //On the click of the 'Send' button, get the value from the text box and emit it
        document.querySelector('#sendBtn').onclick = () => {
            var message = document.querySelector('#msg').value;
            document.querySelector('#msg').value = "";
            //Triggers a custom 'messaging' event
            socket.emit('messaging', usr_name + ": " + message); //const usr_name in index.html
        }
        updateScroll("messages");
    }

});

function scrollSmoothToBottom (id) {
    var div = document.getElementById(id);
    $('#' + id).animate({
       scrollTop: (div.scrollHeight) - (div.clientHeight - 95)
    }, 500);
 }

 function updateScroll(id){
    var element = document.getElementById(id);
    element.scrollTop = element.scrollHeight;
}