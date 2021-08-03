from os import name
from flask import Flask, redirect, url_for, render_template, request, session, flash



app = Flask(__name__)
app.secret_key = "thisisasecret"


@app.route("/")
def home():
    if "name" not in session:
        return redirect(url_for("login"))
    name = session["name"]
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
    session.pop("name", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)