document.addEventListener('DOMContentLoaded', () => {

    if (window.location.pathname == "/"){
        var socket = io.connect('http://' + document.domain + ':' + location.port);
        socket.on('event', data => {
            console.log("Message recieved: " + data)
            var text = document.createTextNode(data + "\n");
            document.getElementById('msgArea').append(text);
          

        });
        document.querySelector('#sendBtn').onclick = () => {
            var message = document.querySelector('#msg').value;
            document.querySelector('#msg').value = "";
            socket.emit('event', usr_name + ": " + message); //const usr_name in index.html
        }

    }

});
