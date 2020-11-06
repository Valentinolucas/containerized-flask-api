from app import app
from app import models as md
from flask import jsonify, request

@app.route("/")
def index():
    return "Hello from flask"

# Post an Order in the database
@app.route("/order", methods = ["POST"])
def add_order():
    order_id = request.json['order_id']
    qty = request.json['qty']
    number = request.json['number']
    customer = request.json['customer']
    email = request.json['email']
    product = request.json['product']
    status = request.json['status']
    note = request.json['note']
    identification = request.json['identification']
    city = request.json['city']
    province = request.json['province']
    
    new_order = md.Order(
        order_id = order_id,
        qty = qty,
        number = number,
        customer = customer,
        email = email,
        product = product,
        status = status,
        note = note,
        identification = identification,
        city = city,
        province = province
    )

    md.db.session.add(new_order)
    md.db.session.commit()
    return md.order_schema.jsonify(new_order)

# Get Orders
@app.route("/api/order", methods = ['GET'])
def get_orders():
    #Check if orders exist
    orders = md.Order.query.all()
    if orders is None:
        return jsonify({"error":"No orders in database"}), 422
    result = md.orders_schema.dump(orders)
    return jsonify(result)


# Get orders by product
@app.route("/api/order/<product>", methods = ["GET"])
def get_by_product(product):
    #Check if orders exist
    orders = md.Order.query.filter_by(product = product)
    if orders is None:
        return jsonify({"error":"No orders in database"}), 422
    result = md.orders_schema.dump(orders)
    return jsonify(result)


# Get orders by status
@app.route("/api/order/status/<status>", methods = ["GET"])
def get_by_status(status):
    #Check if orders exist
    orders = md.Order.query.filter_by(status = status)
    if orders is None:
        return jsonify({"error":"No orders in database"}), 422 
    result = md.orders_schema.dump(orders)
    return jsonify(result)


# Get single product by id
@app.route("/api/order/id/<id>", methods = ["GET"])
def get_by_id(id):
    orders = md.Order.query.get(id)
    if orders is None:
        return jsonify({"error":"No order in database"}), 422
    return md.order_schema.jsonify(orders)


# Update order by id
@app.route("/api/order/id/<id>", methods = ["PUT"])
def update_product(id):
    order = md.Order.query.get(id)
    if order is None:
        return jsonify({"error":"No order in database"}), 422
    
    # Update product in database
    order_id = request.json['order_id']
    qty = request.json['qty']
    number = request.json['number']
    customer = request.json['customer']
    email = request.json['email']
    product = request.json['product']
    status = request.json['status']
    note = request.json['note']
    identification = request.json['identification']
    city = request.json['city']
    province = request.json['province']

    order.order_id = order_id
    order.qty = qty
    order.number = number
    order.customer = customer 
    order.email = email
    order.product = product
    order.status = status
    order.note = note
    order.identification = identification
    order.city = city
    order.province = province

    md.db.session.commit()
    return md.order_schema.jsonify(order)


#Delete order
@app.route("/api/order/id/<id>", methods = ["DELETE"])
def delete_by_id(id):
    order = md.Order.query.get(id)
    # Check if order exist
    if order is None:
        return jsonify({"error":"No order in database"}), 422
    
    # Delete order from database
    md.db.session.delete(order)
    md.db.session.commit()
    return jsonify({"Success":"order has been deleted"}), 200

