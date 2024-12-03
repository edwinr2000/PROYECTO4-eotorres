from flask import Blueprint, jsonify
from api.Models.database import session
from api.Models.ingredient import Ingredient

ingredient_bp = Blueprint('ingredient', __name__, url_prefix='/api/ingredients')

@ingredient_bp.route('/', methods=['GET'])
def get_all_ingredients():
    ingredients = session.query(Ingredient).all()
    return jsonify([ingredient.to_dict() for ingredient in ingredients])

@ingredient_bp.route('/<int:ingredient_id>', methods=['GET'])
def get_ingredient_by_id(ingredient_id):
    ingredient = session.query(Ingredient).get(ingredient_id)
    if not ingredient:
        return jsonify({'error': 'Ingrediente no encontrado'}), 404
    return jsonify(ingredient.to_dict())

@ingredient_bp.route('/name/<string:ingredient_name>', methods=['GET'])
def get_ingredient_by_name(ingredient_name):
    ingredient = session.query(Ingredient).filter_by(name=ingredient_name).first()
    if not ingredient:
        return jsonify({'error': 'Ingrediente no encontrado'}), 404
    return jsonify(ingredient.to_dict())

@ingredient_bp.route('/healthy/<int:ingredient_id>', methods=['GET'])
def is_ingredient_healthy(ingredient_id):
    ingredient = session.query(Ingredient).get(ingredient_id)
    if not ingredient:
        return jsonify({'error': 'Ingrediente no encontrado'}), 404
    return jsonify({'id': ingredient.id, 'name': ingredient.name, 'is_healthy': ingredient.is_healthy})
