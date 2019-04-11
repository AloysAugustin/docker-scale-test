from flask import Flask
import socket

app = Flask(__name__)


@app.route("/")
def hello():
    return f'Hello! My name is { socket.gethostname() }'


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
