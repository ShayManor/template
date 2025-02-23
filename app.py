from flask import Flask, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# Write code here

@app.route("/", methods=["GET"])
def index():
    return send_from_directory(".", "templates/index.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
