from flask import Flask, jsonify  # Correct import of Flask
from flask_cors import CORS
from flask_migrate import Migrate
from models import db, Product  # Assuming `Product` is the model you want to use

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///product.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {"pool_pre_ping": True}

migrate = Migrate(app, db)
db.init_app(app)
CORS(app)  # Initialize CORS here

@app.route('/product', methods=['GET'])
def get_products():
    products = Product.query.all()  # Query all products
    return jsonify([product.to_dict() for product in products]), 200

if __name__ == '__main__':
    app.run(port=5555, debug=True)
