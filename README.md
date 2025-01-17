# eCommerce Using Django

An eCommerce web application built with Django. This project allows users to browse products, add items to their shopping cart, and includes session-based cart management.

## Features

- **Product Browsing**: Users can view a list of available products with images and prices.
- **Shopping Cart**: Session-based cart management to add, update, and remove items.
- **Checkout (Doesn't work)**: Displays the cart total and prepares the user for the checkout process.
- **Responsive Design (barely)**: Frontend designed for usability on both desktop and mobile devices.
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
   ```python3 -m venv env
   source env/bin/activate   # For Linux/macOS
   env\Scripts\activate 
