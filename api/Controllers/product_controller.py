from flask import Blueprint, jsonify
from Models.database import session
from Models.product import Product

product_bp = Blueprint('product', __name__, url_prefix='/api/products')

@product_bp.route('/', methods=['GET'])
def get_all_products():
    products = session.query(Product).all()
    return jsonify([product.to_dict() for product in products])

@product_bp.route('/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    product = session.query(Product).get(product_id)
    if not product:
        return jsonify({'error': 'Producto no encontrado'}), 404
    return jsonify(product.to_dict())

@product_bp.route('/name/<string:product_name>', methods=['GET'])
def get_product_by_name(product_name):
    product = session.query(Product).filter_by(name=product_name).first()
    if not product:
        return jsonify({'error': 'Producto no encontrado'}), 404
    return jsonify(product.to_dict())

@product_bp.route('/calories/<int:product_id>', methods=['GET'])
def get_calories_by_product_id(product_id):
    product = session.query(Product).get(product_id)
    if not product:
        return jsonify({'error': 'Producto no encontrado'}), 404
    return jsonify({'id': product.id, 'name': product.name, 'calories': product.calories})

@product_bp.route('/profitability/<int:product_id>', methods=['GET'])
def get_profitability_by_product_id(product_id):
    product = session.query(Product).get(product_id)
    if not product:
        return jsonify({'error': 'Producto no encontrado'}), 404
    profitability = product.price - (product.calories * 0.01)
    return jsonify({'id': product.id, 'name': product.name, 'profitability': profitability})


@product_bp.route('/cost/<int:product_id>', methods=['GET'])
def get_production_cost(product_id):
    product = session.query(Product).get(product_id)
    if not product:
        return jsonify({'error': 'Producto no encontrado'}), 404
    return jsonify({'id': product.id, 'name': product.name, 'production_cost': product.production_cost})


@product_bp.route('/sell/<int:product_id>', methods=['POST'])
def sell_product(product_id):
    product = session.query(Product).get(product_id)
    if not product:
        return jsonify({'error': 'Producto no encontrado'}), 404
    return jsonify({'message': f'Producto {product.name} vendido con éxito.'})

@product_bp.route('/restock/<int:product_id>', methods=['POST'])
def restock_product(product_id):
    product = session.query(Product).get(product_id)
    if not product:
        return jsonify({'error': 'Producto no encontrado'}), 404
    return jsonify({'message': f'Producto {product.name} reabastecido con éxito.'})


@product_bp.route('/renew/<int:product_id>', methods=['POST'])
def renew_product(product_id):
    product = session.query(Product).get(product_id)
    if not product:
        return jsonify({'error': 'Producto no encontrado'}), 404
    return jsonify({'message': f'Inventario de producto {product.name} renovado con éxito.'})
