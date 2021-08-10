document.addEventListener('DOMContentLoaded', () => {

    if (window.location.pathname == "/"){
        var socket = io.connect('http://' + document.domain + ':' + location.port);
        socket.on('event', data => {
            console.log("Message recieved: " + data)
            var content = `<div class="container" style="
            border: 2px solid #dedede;
            background-color: #f1f1f1;
            border-radius: 5px;
            padding: 10px;
            margin: 10px 0;
            ">` + '<p>' + data + '</p>'
            // var text = document.createTextNode(data + "\n");
            // document.getElementById('msgArea').append(text);
            var updateDiv = document.getElementById("messages");
            updateDiv.innerHTML += content;
            scrollSmoothToBottom("messages")
          

        });
        document.querySelector('#sendBtn').onclick = () => {
            var message = document.querySelector('#msg').value;
            document.querySelector('#msg').value = "";
            socket.emit('event', usr_name + ": " + message); //const usr_name in index.html
        }
    }

});
function scrollSmoothToBottom (id) {
    var div = document.getElementById(id);
    $('#' + id).animate({
       scrollTop: div.scrollHeight - div.clientHeight
    }, 500);
 }