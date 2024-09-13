# Flask Product Management API

    This Flask application provides a RESTful API for managing products. It includes endpoints for adding, retrieving, updating, and deleting products. The application uses SQLAlchemy for database operations and SQLite as the database.

## Requirements

    - Python 3.x
    - Flask
    - Flask-SQLAlchemy
    - Flask-CORS

## Installation

    1. **Clone the repository:**

        ```bash
        git clone <repository-url>
        cd <repository-directory>
        ```

    2. **Create a virtual environment (optional but recommended):**

        ```bash
        python -m venv venv
        source venv/bin/activate  # On Windows use `venv\Scripts\activate`
        ```

    3. **Install the required packages:**

        ```bash
        pip install -r requirements.txt
        ```

    4. **Create the SQLite database and tables:**

        ```bash
        python
        >>> from app import db
        >>> db.create_all()
        ```

## Endpoints

### `/`
    Returns a simple greeting message.
    Hello, There!
## POST /add_product
    Adds a new product to the database.
    Request Body:
    {
    "name": "Product Name",
    "category": "Product Category",
    "description": "Product Description",
    "price": "Product Price"
    }
### Response:
    json
    Copy code
    {
    "message": "product was added successfully!"
    }
## GET /products
    Retrieves all products from the database.

### Response:
    [
    {
        "id": 1,
        "name": "Product Name",
        "category": "Product Category",
        "description": "Product Description",
        "price": "Product Price"
    }
    ]
## PUT /edit_products/<int:id>
    Updates a product's details by its ID.
    Request Body:
    {
    "name": "Updated Name",
    "category": "Updated Category",
    "description": "Updated Description",
    "price": "Updated Price"
    }
### Response:
    {
    "message": "product updated successfully!"
    }
## DELETE /del_products/<int:id>
    Deletes a product by its ID.
### Response:
    {
    "message": "product deleted successfully!"
    }
## Running the Application
    To run the application, use the following command:
    bash
    Copy code
    python app.py
    The application will be available at http://127.0.0.1:5000/.

## Notes
    Ensure that requirements.txt includes the necessary dependencies. You can generate it using pip freeze > requirements.txt.
    The SQLite database file products.db will be created automatically in the same directory as app.py.
    If you encounter any issues or need further assistance, please consult the Flask and SQLAlchemy documentation.