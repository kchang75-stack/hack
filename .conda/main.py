from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

@app.route("/find/<user_id>")
def get_user(user_id):
    data = {
        "item": user_id,
        "lowestPrice": "0",
    }

    return render_template("indextest.html")

@app.route("/test/<search>")
def test(search):
    data = {
        "searchQ": search,
        "value": 4
    }
    print(search)
    return jsonify(data)


if __name__ == "__main__":
    app.run(host="10.140.189.214",port=80, debug=True)