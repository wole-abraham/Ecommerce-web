# eCommerce Using Django

A minimal eCommerce web application built with Django. This project allows users to browse products, add items to their shopping cart, and includes session-based cart management.

## Features

- **Product Browsing**: Users can view a list of available products with images and prices.
- **Product Search**: Users can search for products and view the results.
- **Shopping Cart**: Session-based cart management to add, update, and remove items.
- **Custom Pricing Logic**: Calculates item and total prices dynamically.

## Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Third-Party Service**: Zakeke UI for customizing products (Removed) 
- **Database**: SQLite
- **Session Management**: Django sessions to store cart data

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/wole-abraham/ecommerce-web.git
   cd ecommerce-web
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv env
   source env/bin/activate  # For Linux/macOS
   env\Scripts\activate     # For Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Initialize the database and apply migrations:
   ```bash
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```

5. Create an admin account:
   ```bash
   python3 manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python3 manage.py runserver
   ```

7. Access the application:
   - Main site: [http://127.0.0.1:8000](http://127.0.0.1:8000)
   - Admin panel: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

---

## API Documentation

The API facilitates the integration of Zakeke's UI Customizer and supports basic CRUD operations for products.

### Authentication

- **Account Creation**: Required before accessing API endpoints.
- **Authentication Method**: Basic Auth (username and password).

---
### API in Broswer
You use the api in broswer using the djangorestFramework for more convinience

```http://127.0.0.1:8000/api/products ```


### API Endpoints

| Method  | Endpoint                            | Description                           |
|---------|-------------------------------------|---------------------------------------|
| GET     | `/api/products/`                    | Retrieve all products.                |
| POST    | `/api/products/`                    | Add a new product.                    |
| GET     | `/api/products/<id>/`               | Retrieve details of a specific product. |
| PUT     | `/api/products/<id>/`               | Update a specific product.            |
| DELETE  | `/api/products/<id>/`               | Delete a specific product.            |
| POST    | `/api/products/<id>/customizer/`    | Mark a product as customizable.       |
| DELETE  | `/api/products/<id>/customizer/`    | Unmark a product as customizable.     |

---

### Examples

#### Retrieve All Products
- **URL**: `/api/products/`
- **Method**: `GET`
- **Description**: Fetches all products.
- **Response**:
  ```json
  [
    {
      "id": 12,
      "name": "Polo Shirt",
      "description": "This is a T-shirt",
      "price": "150.00",
      "category": "Fashion",
      "image": "http://127.0.0.1:8000/images/Adult_Polo_Shirt.jpg",
      "stock": 2,
      "thumbnail": "http://127.0.0.1:8000/images/Adult_Polo_Shirt.jpg",
      "customizable": true
    }
  ]
  ```

#### Update a Product
- **URL**: `/api/products/<id>/`
- **Method**: `PUT`
- **Description**: Updates details of a specific product.
- **Request Payload**:
  ```json
  {
    "name": "Updated Product",
    "price": 40.00,
    "description": "Updated description"
  }
  ```
- **Response**:
  ```json
  {
    "id": 1,
    "name": "Updated Product",
    "price": 40.00,
    "description": "Updated description"
  }
  ```

#### Delete a Product
- **URL**: `/api/products/<id>/`
- **Method**: `DELETE`
- **Description**: Deletes a specific product.
- **Response**:
  ```json
  {
    "message": "Product deleted successfully"
  }
  ```

#### Mark a Product as Customizable
- **URL**: `/api/products/<id>/customizer/`
- **Method**: `POST`
- **Description**: Marks a product as customizable.
- **Response**:
  ```json
  {
    "message": "Product {product_name} is now customizable"
  }
  ```

#### Unmark a Product as Customizable
- **URL**: `/api/products/<id>/customizer/`
- **Method**: `DELETE`
- **Description**: Unmarks a product as customizable.
- **Response**:
  ```json
  {
    "message": "Product {product_name} is no longer customizable"
  }
  
