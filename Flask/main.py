from flask import Flask, redirect, url_for, render_template, request, session, flash
#from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "dog"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#app.permanent_session_lifetime = timedelta(seconds=30)

db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/view")
def view():
    return render_template("view.html", values = users.query.all())

@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        #session.permanent = True
        user_name = request.form["user_name"]  #Get user_name from login.html
        while user_name == "":
            user_name = request.form["user_name"]
        session["user"] = user_name  #Give key "user" in session a value as user_name
        
        found_user = users.query.filter_by(name = user_name).first()
        if found_user:
            session["input_email"] = found_user.email
        else:
            usr = users(user_name, "")
            db.session.add(usr)
            db.session.commit()
        
        flash("Loged in ok")
        return redirect(url_for("user"))
    else:
        if "user" in session:  #If this user session is open
            flash("Login already")
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/user", methods = ["POST", "GET"])
def user():
    email = None  #Var = None so input_email is clear each login time
    if "user" in session:
        user_name = session["user"]
        if request.method == "POST":
            email = request.form["input_email"]  #Get input_email from user.html
            session["input_email"] = email  #Give key "input_email" in session a value as var email 
            found_user = users.query.filter_by(name = user_name).first()  #Found user name in database
            found_user.email = email  #Put user email into input_email in user.html
            db.session.commit()
            flash("Email saved")
        else:
            if "input_email" in session:  #Check if session of input_email is open
                email = session["input_email"]  #Then var email == input_email
        return render_template("user.html", email = email)  #Place email into input in user.html
    else:
        flash("Not login yet")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    flash("Loged out")
    session.pop("user", None)
    session.pop("input_email", None)  #Must pop input_email
    return redirect(url_for("login"))

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)