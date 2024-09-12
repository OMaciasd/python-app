import logging
from flask import Flask
from waitress import serve

# Configuración de logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)


@app.route("/")
def index():
    return "Welcome to Flask!"


if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=8080)
