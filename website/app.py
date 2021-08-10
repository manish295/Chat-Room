from Db.database import Database
from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask_socketio import SocketIO, emit, send
users = []

app = Flask(__name__)
app.secret_key = "thisisasecret"
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
        flash(f"Logged in as {name}")
        return redirect(url_for("home"))

    
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("name", None)
    return redirect(url_for("login"))

  


@socketio.on('disconnect')
def disconect_msg():
    print(f'Disconnected!')
    emit("event", session["name"] + ": " + "has left!", broadcast=True)
    users.remove(session["name"])
    if len(users) == 0:
        db = Database()
        db.remove_messages("messages")
        db.close()

@socketio.on('connect')
def connected():
    users.append(session["name"])
    connected_msg = session["name"].replace("'","''") + ": " + "has joined!"
    db = Database()
    messages = db.return_messages("Manish", all=True)
    db.save_messages(session["name"].replace("'","''"), connected_msg)
    db.close()
    for message in messages:
        emit("event", message)
    emit("event", session["name"] + ": " + "has joined!", broadcast=True)


@socketio.on('event')
def handle_custom_event(data):
    print(f'received custom event!: ' + data)
    db = Database()
    db.save_messages(session["name"].replace("'","''"), data.replace("'","''"))
    db.close()
    emit("event", data, broadcast=True)
    
  

if __name__ == "__main__":
   socketio.run(app, debug=True, host="192.168.1.216")

