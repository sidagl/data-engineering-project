import os
from flask import Flask, jsonify, request
from flask import render_template
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect("database/products.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    return {
        "message": "Data Engineering API is running",
        "endpoints": [
            "/products",
            "/avg-price",
            "/top-rated",
            "/products/rating/<rating>",
            "/search?q=keyword"
        ]
    }
@app.route("/dashboard")
def dashboard():
    return render_template("index.html")

#all products
@app.route("/products")
def get_products():
    conn = get_db_connection()
    products = conn.execute("SELECT * FROM products LIMIT 20").fetchall()
    conn.close()

    return jsonify([dict(row) for row in products])


#Filter by rating
@app.route("/products/rating/<int:rating>")
def get_by_rating(rating):
    conn = get_db_connection()
    products = conn.execute(
        "SELECT * FROM products WHERE rating = ?", (rating,)
    ).fetchall()
    conn.close()

    return jsonify([dict(row) for row in products])
#Average price
@app.route("/avg-price")
def avg_price():
    conn = get_db_connection()
    result = conn.execute(
        "SELECT AVG(price) as avg_price FROM products"
    ).fetchone()
    conn.close()

    return jsonify(dict(result))
#Top rated products
@app.route("/top-rated")
def top_rated():
    conn = get_db_connection()
    products = conn.execute(
        "SELECT * FROM products ORDER BY rating DESC LIMIT 10"
    ).fetchall()
    conn.close()

    return jsonify([dict(row) for row in products])
#Search by name
@app.route("/search")
def search():
    query = request.args.get("q", "")

    conn = get_db_connection()
    products = conn.execute(
        "SELECT * FROM products WHERE name LIKE ?",
        (f"%{query}%",)
    ).fetchall()
    conn.close()

    return jsonify([dict(row) for row in products])


# if __name__ == "__main__":
#     app.run(debug=True)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
