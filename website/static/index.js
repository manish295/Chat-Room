$(function() {
    $('#sendBtn').on('click', function(e) {
    e.preventDefault()
    var value = document.getElementById("msg").value
    $.getJSON('/run',
        {val:value},
        function(data) {
            
    });
    return false;
    });
});
