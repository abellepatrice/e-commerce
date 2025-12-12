# E-Commerce API

A Flask-based REST API for an e-commerce platform, featuring user authentication, product management, and order handling using MongoDB as the database.

## Features

- **User Authentication**: Secure user registration and login with JWT tokens.
- **Product Management**: Add and retrieve products.
- **Order Management**: Create and view orders for authenticated users.
- **Database**: MongoDB for data storage.
- **Security**: Password hashing and JWT-based authentication.
- **CORS Support**: Enabled for cross-origin requests.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd <project-directory>
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   Create a `.env` file in the root directory with the following:
   ```
   MONGO_URI=mongodb://localhost:27017/ecommerce
   JWT_SECRET_KEY=your-secret-key
   ```

4. Ensure MongoDB is running on your system.

## Usage

Run the application:
```
python app.py
```

The API will be available at `http://localhost:5000`.

## API Endpoints

### Authentication
- `POST /api/auth/register`: Register a new user.
  - Body: `{"username": "string", "password": "string"}`
- `POST /api/auth/login`: Login and receive a JWT token.
  - Body: `{"username": "string", "password": "string"}`

### Products
- `GET /api/products`: Retrieve all products.
- `POST /api/products`: Add a new product (requires authentication?).
  - Body: Product data (e.g., `{"name": "string", "price": number}`)

### Orders
- `POST /api/orders`: Create a new order (requires authentication).
  - Body: Order data (e.g., `{"products": [...], "total_price": number}`)
- `GET /api/orders`: Retrieve orders for the authenticated user.

## Project Structure

- `app.py`: Main Flask application.
- `config.py`: Configuration settings.
- `db.py`: Database initialization.
- `models/`: Data models (User, Order, Product).
- `routes/`: API route handlers (auth, orders, products).
- `requirements.txt`: Python dependencies.

## Contributing

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Submit a pull request.

## License

This project is licensed under the MIT License.
