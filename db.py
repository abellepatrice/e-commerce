from flask_pymongo import PyMongo

# Create a PyMongo instance without initializing it directly
mongo = PyMongo()

# Function to initialize the PyMongo instance with the Flask app
def init__db(app):
    """
    Initialize the MongoDB connection with the Flask application.

    :param app: The Flask application instance
    :return: Initialized PyMongo instance
    """
    # Initialize the mongo instance with the Flask app
    mongo.init__app(app)
    return mongo
