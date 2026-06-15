from flask import Flask, render_template
import os
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "index.html",
        hostname=socket.gethostname(),
        version="v3.0",
        environment="Development",
        app_name="Flask GitOps Demo"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)