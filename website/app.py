from threading import Thread
import time
from Server.Db.database import *
from flask import Flask, json, redirect, url_for, render_template, request, session, flash, jsonify
from Client.client import Client
app = Flask(__name__)
app.secret_key = "thisisasecret"

first_message = True
second_message = True

@app.route("/")
def home():
    global client
    global name
    if "name" not in session:
        return redirect(url_for("login"))
    
    name = session["name"]
    client = Client(name)
    return render_template("index.html", name=name)

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
    client.send_msg("!DISCONNECT")
    session.pop("name", None)
    return redirect(url_for("login"))

@app.route("/run/", methods=["GET"])
def run():
    msg = request.args.get("val")
    client.send_msg(msg)
    # print(client.msgs)

    return "none"

@app.route("/get_msgs", methods=['POST', 'GET'])
def get_msgs():
    global first_message
    time.sleep(0.2)
    if first_message:
        updated_message = "".join(client.msgs[0:3])
        print(updated_message)
        client.msgs.clear()
        first_message = False
        return jsonify({"message": updated_message})

    else:
        updated_message = "".join(client.msgs)
        print(updated_message)
        client.msgs.clear()
        return jsonify({"message": updated_message})

    # for msg in msgs:
    #     return jsonify(msg)


# def update_messages():
#     #print(client.msgs)
#     for msg in client.msgs:
#         return msg




if __name__ == "__main__":
    app.run(debug=True)


