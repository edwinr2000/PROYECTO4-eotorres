from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from api.Models.database import session
from api.Models.user import User

auth_bp = Blueprint('auth', __name__, template_folder='../templates')

# Ruta para la página inicial
@auth_bp.route('/')
def home():
    return render_template('index.html')

# Ruta para inicio de sesión
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Buscar el usuario en la base de datos
        user = session.query(User).filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            flash(f"¡Bienvenido, {user.username}!", "success")

            # Redirige según el rol
            if user.es_admin:
                return redirect(url_for('auth.admin_dashboard'))
            elif user.es_empleado:
                return redirect(url_for('auth.employee_dashboard'))
            else:
                return redirect(url_for('auth.user_dashboard'))
        else:
            flash('Usuario o contraseña incorrectos', 'danger')

    return render_template('login.html')

# Ruta para cerrar sesión
@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesión correctamente.', 'info')
    return redirect(url_for('auth.login'))

# Ruta para el dashboard de admin
@auth_bp.route('/admin', methods=['GET'])
@login_required
def admin_dashboard():
    if not current_user.es_admin:
        return render_template('error.html'), 403

    # Obtener todos los productos e ingredientes
    from Models.product import Product
    from Models.ingredient import Ingredient
    products = session.query(Product).all()
    ingredients = session.query(Ingredient).all()

    # Verificar que se estén recuperando datos correctamente
    print(f"Productos: {products}")
    print(f"Ingredientes: {ingredients}")

    return render_template('admin_dashboard.html', products=products, ingredients=ingredients)

# Ruta para el dashboard de empleados
@auth_bp.route('/employee', methods=['GET'])
@login_required
def employee_dashboard():
    if not current_user.es_empleado:
        return render_template('error.html'), 403

    # Obtener todos los productos e ingredientes
    from Models.product import Product
    from Models.ingredient import Ingredient

    # Asegurarse de que se recuperan los productos e ingredientes
    products = session.query(Product).all()
    ingredients = session.query(Ingredient).all()

    # Verificar que se están recuperando los datos correctamente
    print(f"Productos: {len(products)} productos encontrados.")
    print(f"Ingredientes: {len(ingredients)} ingredientes encontrados.")

    return render_template('employee_dashboard.html', products=products, ingredients=ingredients)



# Ruta para manejar errores de acceso
@auth_bp.route('/error', methods=['GET'])
def error():
    return render_template('error.html'), 403
