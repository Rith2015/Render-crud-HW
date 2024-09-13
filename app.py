from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
app=Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Optional, to disable track modifications
db=SQLAlchemy(app)
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(80),unique=True, nullable=False)
    category=db.Column(db.String(130), nullable=False)
    description=db.Column(db.String(200), nullable=False)
    price=db.Column(db.String(120),nullable=False)
    def __repr__(self):
                return f'<Product {self.name}>'
@app.route('/')
def home():
    return 'Hello, There!'
# adds new items to list
@app.route('/add_product',methods=['POST'])
def add():
    data=request.json
    new_item=Product(
        name=data['name'],
        category=data['category'],
        description=data['description'],
        price=data['price']  
      )
    db.session.add(new_item)
    db.session.commit()
    return jsonify({"message": "product was added successfully!"}), 201
# show all products in list
@app.route('/products',methods=['GET'])
def show_data():
      products=Product.query.all()
      return jsonify([{'id': item.id, 'name': item.name, 'category': item.category, 'description': item.description, 'price': item.price}for item in products])
# edit item in list by id
@app.route('/edit_products/<int:id>', methods=['PUT'])
def update_data(id):
    data=request.json
    item=Product.query.get(id)
    if item:
        item.name=data.get('name', item.name)
        item.category=data.get('category', item.category)
        item.description=data.get('description', item.description)
        item.price=data.get('price', item.price)
        db.session.commit()
        return jsonify({'message': 'product updated successfully!'})
    else:
        return jsonify({"message": "product not found!"}), 404
# delets items by id
@app.route('/del_products/<int:id>', methods=['DELETE'])
def delete_data(id):
    item=Product.query.get(id)
    if item:
        db.session.delete(item)
        db.session.commit()
        return jsonify({'message': 'product deleted successfully!'})
    else:
        return jsonify({"message": "product not found!"}), 404
    
if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)