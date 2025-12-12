from flask import Blueprint, request, jsonify
from app import db

products_bp = Blueprint('products', __name__)

@products_bp.route('/', methods=['GET'])
def get_products():
    products = list(db.products.find())
    for product in products:
        product['_id'] = str(product['_id'])
    return jsonify(products), 200

@products_bp.route('/', methods=['POST'])
def add_product():
    data = request.get_json()
    db.products.insert_one(data)
    return jsonify({'message': 'Product added successfully'}), 201
