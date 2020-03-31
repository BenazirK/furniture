from flask import Flask, render_template
shop= Flask(__name__)

@shop.route("/")
def homepage():
    return "<h1>Добро пожаловать в магазин мебели</h1>"

@shop.route("/types")
def types():
    return render_template ("types.html")

@shop.route("/kitchen")
def kitchen():
    return render_template ("kitchen.html")

@shop.route("/proposal/<name>")
def proposal(name):
    name = name.capitalize()
    return render_template("proposal.html", name=name)

