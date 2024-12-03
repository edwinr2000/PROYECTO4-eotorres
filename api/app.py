import os
import logging
from flask import Flask, render_template
from flask_login import LoginManager, current_user
from api.Controllers.product_controller import product_bp
from api.Controllers.ingredient_controller import ingredient_bp
from api.Controllers.auth_controller import auth_bp
from api.Models.database import session
from api.Models.user import User

# Configuración de logs
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

# Clave secreta para manejo de sesiones (asegúrate de que la variable de entorno esté definida)
app.secret_key = os.environ.get("clave_super_segura_para_desarrollo", "una_clave_predeterminada_segura")

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
        app.logger.error(f"Error cargando el usuario: {e}")
        return None

# Verificar conexión a la base de datos
try:
    session.execute("SELECT 1")
    app.logger.debug("Conexión a la base de datos exitosa.")
except Exception as e:
    app.logger.error(f"Error al conectar con la base de datos: {e}")

# Registrar blueprints
try:
    app.register_blueprint(product_bp)
    app.logger.debug("Blueprint product_bp registrado correctamente.")
except Exception as e:
    app.logger.error(f"Error al registrar product_bp: {e}")

try:
    app.register_blueprint(ingredient_bp)
    app.logger.debug("Blueprint ingredient_bp registrado correctamente.")
except Exception as e:
    app.logger.error(f"Error al registrar ingredient_bp: {e}")

try:
    app.register_blueprint(auth_bp)
    app.logger.debug("Blueprint auth_bp registrado correctamente.")
except Exception as e:
    app.logger.error(f"Error al registrar auth_bp: {e}")

@app.context_processor
def inject_user():
    return dict(current_user=current_user)

@app.route('/')
def index():
    try:
        app.logger.debug("Intentando renderizar index.html")
        return render_template('index.html')
    except Exception as e:
        app.logger.error(f"Error al renderizar index.html: {e}")
        return "Error al cargar la página de inicio.", 500