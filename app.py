from flask import Flask, render_template
from flask_login import LoginManager, current_user
from Controllers.product_controller import product_bp
from Controllers.ingredient_controller import ingredient_bp
from Controllers.auth_controller import auth_bp
from Models.database import session
from Models.user import User

app = Flask(__name__)

# Clave secreta para manejo de sesiones
app.secret_key = 'clave_super_segura_para_desarrollo'

# Configuración de Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'
login_manager.login_message = "Por favor inicia sesión para acceder a esta página."

@login_manager.user_loader
def load_user(user_id):
    try:
        return session.query(User).get(int(user_id))
    except Exception as e:
        print(f"Error cargando el usuario: {e}")
        return None

# Registrar blueprints
app.register_blueprint(product_bp)
app.register_blueprint(ingredient_bp)
app.register_blueprint(auth_bp)

@app.context_processor
def inject_user():
    return dict(current_user=current_user)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


#Test