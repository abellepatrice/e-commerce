from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from config import Config
from db import init__db  # Import the database initialization function

app = Flask(__name__)
app.config.from_object(Config)  # Load configuration from Config class

# Initialize Flask extensions
jwt = JWTManager(app)
CORS(app)

# Initialize the database
db = init__db(app)

# Import and register the auth blueprint
from routes.auth import auth_bp  # Ensure the path to auth.py is correct
app.register_blueprint(auth_bp, url_prefix='/api/auth')

if __name__ == '__main__':
    app.run(debug=True)
