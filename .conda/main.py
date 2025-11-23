from flask import Flask, request, jsonify, render_template
from parse_controller import parse
import sqlite3
from database_manager import DatabaseManager
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

    parse(search)

    queries = [query for query in search.split(", ") if query.split()]
    for query in queries:
        top_five = DatabaseManager.get_prices_by_product(query, query)[:5]

    data = {
        # "searchQ": search,
        "value": 4,
        "Item_Name": [item["itemName"] for item in top_five],
        "Item_Price": [item["itemPrice"] for item in top_five],
        "Store_Name": [item["storeName"] for item in top_five],
        "Query_Value": [item["query"] for item in top_five]
    }

    return jsonify(data)


if __name__ == "__main__":
    app.run(host="192.168.56.1",port=80, debug=True)
