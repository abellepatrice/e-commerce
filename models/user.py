from flask import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash

mongo = PyMongo()  # Make sure to initialize this with the app context

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)  # Hash password for security

    def save(self):
        """Save user to the MongoDB database."""
        user_data = {
            "username": self.username,
            "email": self.email,
            "password": self.password
        }
        mongo.db.users.insert_one(user_data)

    @staticmethod
    def find_by_username(username):
        """Find a user by their username."""
        return mongo.db.users.find_one({"username": username})

    def check_password(self, password):
        """Check the hashed password."""
        return check_password_hash(self.password, password)
