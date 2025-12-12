from flask import Blueprint, request, jsonify
from app import db
from flask_jwt_extended import jwt_required, get_jwt_identity

orders_bp = Blueprint('orders', __name__)

@orders_bp.route('/', methods=['POST'])
@jwt_required()
def create_order():
    current_user = get_jwt_identity()
    data = request.get_json()
    data['user'] = current_user['username']
    db.orders.insert_one(data)
    return jsonify({'message': 'Order created successfully'}), 201

@orders_bp.route('/', methods=['GET'])
@jwt_required()
def get_orders():
    current_user = get_jwt_identity()
    orders = list(db.orders.find({'user': current_user['username']}))
    for order in orders:
        order['_id'] = str(order['_id'])
    return jsonify(orders), 200
