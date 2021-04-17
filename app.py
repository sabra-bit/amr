from flask import Flask, redirect, url_for, render_template, request
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"] )
def welcome():
    mname = request.form["Uname"]
    mcode = request.form["Pass"]
    if mname == 'amr' and mcode == '123' :
        return render_template("login.html")
    else:
        return "<h1>NOT ALLOWED</h1>" 


@app.route("/last", methods=["POST", "GET"] )
def last(): 
    return render_template("last.html")
    
if __name__ == '__main__':
    app.run(debug= True)