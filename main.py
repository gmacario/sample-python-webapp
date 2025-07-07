"""
# main.py
# This script sets up a simple Flask web application with a single endpoint.
"""

from flask import Flask, jsonify

def main():
    app = Flask(__name__)

    @app.route("/hello", methods=["GET"])
    def hello():
        return jsonify(message="Hello from Flask endpoint!"), 200

    app.run(host="0.0.0.0", port=5000)


if __name__ == "__main__":
    main()
