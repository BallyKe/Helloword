#coding=utf-8

from flask import Flask

app = Flask(__name__)
@app.route("/")

def init():
    return "Hello word."

if __name__ == "__main__":
    app.debug = True
    app.run()
