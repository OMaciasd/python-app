from flask import Flask, render_template
import logging
from waitress import serve

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__, template_folder='templates')


@app.route("/")
def index():
    print("Llamando a la función index()")
    return render_template("index.html")


@app.route("/hello/<name>")
def hello(name):
    return f"Hola, {name}!"


@app.route("/template")
def template():
    return render_template("index.html")


if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=8000)
