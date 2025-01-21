# eCommerce Using Django

An Minimal eCommerce web application built with Django. This project allows users to browse products, add items to their shopping cart, and includes session-based cart management.

## Features

- **Product Browsing**: Users can view a list of available products with images and prices.
- **Product Search**: Users can search for a product and get results
- **Shopping Cart**: Session-based cart management to add, update, and remove items.
- **Custom Pricing Logic**: Calculates item and total prices dynamically.

## Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Third-Party Service**: Zakeke UI for customizing products
- **Database**: SQLite
- **Session Management**: Django sessions to store cart data

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/wole-abraham/ecommerce-web.git
   cd ecommerce-web
2. Create a virtual environment:
   ```
   python3 -m venv env
   source env/bin/activate   # For Linux/macOS
   env\Scripts\activate # for Windows
   
3. Install dependencies
   ```
   pip install -r requirements.txt

4. Initialize the database and Make Migrations
   ```
   python3 manage.py makemigrations
   python3 manage.py migrate

5. Create Admin Account
   ```
   Python3 manage.py createsuperuser
   
6. Run the development server
   ```
   python3 manage.py runserver 5000
   
7. visit the site (http:127.0.0.1:5000)
   
7. Visit the Admin page to manage products(http:127.0.0.1:5000/admin)
   

   ## API DOCUMENTATION
   The API is built to accomodate the intergration of zakeke's UI       Customizer
   ## Endpoints
   **Before using the api, an account creation is needed**
   **The Api enforces Basic Auth(username and password is required)**
   

                                             | Method    | Endpoint                         | Description                     |
                                             |-----------|----------------------------------|---------------------------------|
                                             | GET       | `/api/products/`                 | Retrieve all products.          |
                                             | POST      | `/api/products/`                 | Add a new product.              |
                                             | GET       | `/api/products/<id>`             | Retrieve details of a product.  |
                                             | PUT       | `/api/products/<id>`             | Update a specific product.      |
                                             | DELETE    | `/api/products/<id>`             | Delete a specific product.      |
                                             | POST      | `/api/product/<id>/customizer`   | Marks a product as customizable|
   ### **Retrieve All Products **
   - **URL**: `/api/products/`
   - **METHOD**: `GET`
   - **DESCRIPTION**: Fetches all Products.
   - **Response**:
     ```[ {
        "values": [],
        "code": "12",
        "name": "Polo Shirt",
        "description": "This is T-shirt",
        "price": "150.00",
        "category": Fashion,
        "image": "http://127.0.0.1:5000/images/images/Adult_Polo_Shirt.jpg",
        "stock": 2,
        "thumbnail": "http://127.0.0.1:5000/images/images/Adult_Polo_Shirt.jpg",
        "customizable": true
    }]
   ```
- **Code**: The product Id
- **name**: Product name
- **decscription**: Product description
- **image**: Absolute url of the image stored on the server
  
### **Update a Product**
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

---

---

### **Delete a Product**
- **URL**: `/api/products/<id>/`
- **Method**: `DELETE`
- **Description**: Deletes a specific product.
- **Response**:
    ```json
    {
      "message": "Product deleted successfully"
    }
    ```

---
