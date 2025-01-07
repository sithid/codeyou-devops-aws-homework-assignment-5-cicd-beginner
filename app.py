from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Flask App!"})


@app.route("/health")
def health():
    return jsonify({"status": "OK"}), 200


if __name__ == "__main__":
    app.run(debug=False)
