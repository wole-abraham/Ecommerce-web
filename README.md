# eCommerce Using Django

An eCommerce web application built with Django. This project allows users to browse products, add items to their shopping cart, ait includes session based management 

## Features

- **Product Browsing**: Users can view a list of available products with images and prices.
- **Shopping Cart**: Session-based cart management to add, update, and remove items.
- **Checkout(Doesn't work)**: Displays the cart total and prepares the user for the checkout process.
- **Responsive Design(barely)**: Frontend designed for usability on both desktop and mobile devices.
- **Custom Pricing Logic**: Calculates item and total prices dynamically.

## Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Thirparty Serive**: Zakeke UI for Customizing products
- **Database**: SQLite
- **Session Management**: Django sessions to store cart data

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/wole-abraham/ecommerce-web.git
   cd ecommerce-web
2. Create a Virtual Environment
``` python3 -m venv env
source env/bin/activate   # For Linux/macOS
env\Scripts\activate      # For Windows
3. ```pip install -r requirements.txt
4. ```python manage.py runserver
5. Goto your browser 127.0.0.1:5000


