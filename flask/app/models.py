from app import app
import datetime
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 

# Init db
db = SQLAlchemy(app)

# Init Marshmallow
ma = Marshmallow(app)

# Create Model
class Order(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    order_id = db.Column(db.Integer)
    qty = db.Column(db.Integer)
    number = db.Column(db.String(64))
    customer = db.Column(db.String(64))
    email = db.Column(db.String(64))
    product = db.Column(db.String(64))
    status = db.Column(db.String(64))
    note = db.Column(db.Text(255))
    date = db.Column(db.DateTime, default = datetime.datetime.now)
    identification = db.Column(db.String(64))
    city = db.Column(db.String(64))
    province = db.Column(db.String(64))

    def __init__(self, order_id, qty, number, customer, email, product, status, note, identification, city, province):
        self.order_id = order_id
        self.qty = qty
        self.number = number
        self.customer = customer
        self.email = email
        self.product = product
        self.status = status
        self.note = note
        self.identification = identification
        self.city = city
        self.province = province

# Create Schema
class OrderSchema(ma.Schema):
    class Meta:
        fields = ('id', 'order_id', 'qty', 'number', 'customer', 'email', 'product', 'status', 'note', 'date', 'identification', 'city', 'province')

order_schema = OrderSchema()
orders_schema = OrderSchema(many = True)