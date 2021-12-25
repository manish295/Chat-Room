from Db.database import Database
from flask import Flask, redirect, url_for, render_template, request, session
from flask_socketio import SocketIO, emit
import os
users = []

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET')
socketio = SocketIO(app)

@app.route("/")
def home():
    if "name" not in session:
        return redirect(url_for("login"))
    

    name = session["name"]
    
    return render_template("index.html", usr_name=name)


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        name = request.form["nm"]
        session["name"] = name
        return redirect(url_for("home"))

    
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("name", None)
    return redirect(url_for("login"))

"""
Triggers when a user disconnects
Emit a leaving message
If no users are in the chat, delete the messages in db
"""
@socketio.on('disconnect')
def disconect_msg():
    print(f'Disconnected!')
    emit("messaging", session["name"] + ": " + "has left!", broadcast=True)
    users.remove(session["name"])
    if len(users) == 0:
        db = Database()
        db.remove_messages()
        db.close()

""""
Triggers on 'connect' event
Emit all the previous messages and a welcome message
"""
@socketio.on('connect')
def connected():
    users.append(session["name"])
    connected_msg = session["name"].replace("'","''") + ": " + "has joined!"
    db = Database()
    messages = db.return_messages()
    db.add_message(session["name"].replace("'", "''"), connected_msg)
    db.close()
    for message in messages:
        emit("messaging", message)
    emit("messaging", session["name"] + ": " + "has joined!", broadcast=True)

"""
Triggers on 'messaging' event
Store message sent from client and emit the message back
"""
@socketio.on('messaging')
def handle_custom_event(data):
    print(f'received custom event!: ' + data)
    db = Database()
    db.add_message(session["name"].replace("'","''"), data.replace("'","''"))
    db.close()
    emit("messaging", data, broadcast=True) 
    
  

if __name__ == "__main__":
   app.run()