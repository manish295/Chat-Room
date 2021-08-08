document.addEventListener('DOMContentLoaded', () => {
    var socket = io.connect('http://' + document.domain + ':' + location.port);
    // socket.on('connect', () => {
    //             socket.send("I am connected!");
    //             });
        
    socket.on('message', data => {
                console.log("Message recieved: " + data)
                // var text = document.createTextNode(data + "\n");
                // document.getElementById('msgArea').append(text);
                console.log(data);
                const p = document.createElement('p');
                const br = document.createElement('br');
                p.innerHTML = data;
                document.querySelector('#msg-section').append(p);

            });
    
    document.querySelector('#sendBtn').onclick = () => {
        var message = document.querySelector('#msg').value;
        socket.send(usr_name + ": " + message); //const usr_name in index.html
    }

});
