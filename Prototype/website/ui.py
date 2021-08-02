from flask import Flask, redirect, url_for, render_template, request, session, flash



app = Flask(__name__)
app.secret_key = "thisisasecret"


@app.route("/")
def home():
    if "name" not in session:
        return redirect(url_for("login"))
    return None


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        name = request.form["nm"]
        session["name"] = name
        flash("Login Sucessful!")
    
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)