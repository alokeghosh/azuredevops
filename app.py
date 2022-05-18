from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, this is a sample my Python Web App running on Flask Framework!"

