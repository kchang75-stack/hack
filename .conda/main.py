from flask import Flask, request, jsonify, render_template
from parse_controller import parse
import sqlite3
from database_manager import DatabaseManager
import os

app = Flask(__name__)

@app.route("/")
def loadHTML():
    return render_template("indextest.html")

@app.route("/test/<search>")
def test(search):

    parse(search)


    top_five = DatabaseManager.get_prices_by_product(search, search)
    print(top_five)

    data = {
        # "searchQ": search,
        "value": 4,
        "Item_Name": [item[0] for item in top_five],
        "Item_Price": [item[1] for item in top_five],
        "Store_Name": [item[2] for item in top_five],
        "Query_Value": [item[3] for item in top_five]
    }

    return jsonify(data)


if __name__ == "__main__":
    app.run(host="10.140.189.214",port=80, debug=True)
