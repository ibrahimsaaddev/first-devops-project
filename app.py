from flask import Flask
import logging
app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route("/")
def home():
    app.logger.info("Home page visited")
    with open("index.html", "r") as file:
        return file.read()

@app.route("/health")
def health():
    return "OK"

