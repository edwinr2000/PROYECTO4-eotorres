import os
from flask import Flask, render_template
from flask_login import LoginManager
from api.Controllers.product_controller import product_bp
from api.Controllers.ingredient_controller import ingredient_bp
from api.Controllers.auth_controller import auth_bp
from api.Models.database import session
from api.Models.user import User

app = Flask(__name__)

# Clave secreta para manejo de sesiones
app.secret_key = "clave_super_segura_para_desarrollo"

# Configuración de Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return session.query(User).get(user_id)

# Registro de Blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(product_bp)
app.register_blueprint(ingredient_bp)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
