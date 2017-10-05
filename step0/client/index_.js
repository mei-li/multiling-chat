// ----------
// WEBSOCKETS
// ----------

// websocket connection for talking to the server
var server = new WebSocket("ws://" + location.host + "/connect");

// code to run when our websocket connects
server.onopen = function() {
    message = JSON.stringify({"message": "Hello, everybody!"});
    server.send(message);
}

// code to run when we receive a message from the server
server.onmessage = function(message) {
    //console.log(message);
    var m = JSON.parse(message.data);
    if (m.popup) {
        alert(m.popup);
    } else if (m.message) {
        var text = m.client + ": " + m.message
        text = '<span style="color:' + m.color + '">' + text + "</span>"
        document.getElementById('textbox').innerHTML += "<br>" + text;
    }
}

// -------------
// text messages
// -------------

function submit_message() {
    var typebox = document.getElementById('typebox');
    var message = JSON.stringify({"message": typebox.value});
    server.send(message);
    typebox.value = "";
}
