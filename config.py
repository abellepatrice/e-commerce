import os
from dotenv import load_dotenv  # Corrected import

# Load environment variables from .env file
load_dotenv()

class Config:
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/ecommerce")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "supersecretkey")

# You can also define other configurations for different environments if needed.
