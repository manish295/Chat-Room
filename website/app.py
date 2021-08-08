from flask import Flask, redirect, url_for, render_template, request, session, flash, jsonify
from flask_socketio import SocketIO, send


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


@app.route("/get_name", methods=["POST", "GET"])
def get_name():
    if "name" in session:
        name = {"name" : session["name"]}
    return jsonify(name)
  

@socketio.on("message")
def message(data):
    print(f'{data}')
    send(data, broadcast=True)



if __name__ == "__main__":
   socketio.run(app, debug=True, host="192.168.1.216")

