from flask import render_template
from app import app
from models.shop import orders


# @app.route('/')
# def index():
#     return render_template("index.html")

@app.route('/orders')
def index():
    return render_template("index.html", order_list = orders)

@app.route('/orders/<index>')
def order(index):
    return render_template("order.html", item = orders [int(index)])