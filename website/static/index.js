$(function() {
    $('#sendBtn').on('click', function(e) {
    var value = document.getElementById("msg").value
    $.getJSON('/run',
        {val:value},
        function(data) {
            
            
    });
    $.ajax({
        url: '/get_msgs',
        type: 'POST',
        data: $("#sendBtn"),
    })
    .done(function(data) {
        console.log("success " + data.message);
        var text = document.createTextNode(data.message);
        document.getElementById("msgArea").append(text);
        //document.getElementById("msgArea").value = data.message;
    })
    e.preventDefault();
    });
});

// window.addEventListener("load", function() {
//     var update_loop = setInterval(update, 500)
//     update()
// });

// function update() {
//     fetch('/get_msgs')
//     .then(function (response) {
//         return response.text();
//     }).then(function (text) {
//         console.log('GET response text:');
//         console.log(text)
//     // return false;
//     });

// }

 