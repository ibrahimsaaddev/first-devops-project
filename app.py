from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    with open("index.html", "r") as file:
        return file.read()
