from flask_pymongo import PyMongo
from bson.objectid import ObjectId

mongo = PyMongo()  # Initialize with Flask app

class Order:
    def __init__(self, user_id, products, total_price):
        self.user_id = user_id
        self.products = products
        self.total_price = total_price

    def save(self):
        """Save order to the database."""
        order_data = {
            "user_id": self.user_id,
            "products": self.products,
            "total_price": self.total_price,
            "status": "pending"
        }
        mongo.db.orders.insert_one(order_data)

    @staticmethod
    def find_by_user(user_id):
        """Find orders by user ID."""
        return list(mongo.db.orders.find({"user_id": ObjectId(user_id)}))
