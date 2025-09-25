from flask import Flask, render_template, request, redirect, url_for, session, flash
from markupsafe import escape

app = Flask(__name__)
app.secret_key = "cambia_esto_por_una_clave_secreta_larga"  # Cambia en producción

# Inicializar estructura en sesión si no existe
def asegurar_usuarios_en_sesion():
    if 'usuarios' not in session:
        session['usuarios'] = {}
        session.modified = True

@app.route('/')
def index():
    asegurar_usuarios_en_sesion()
    if session.get('usuario'):
        return redirect(url_for('inicio'))
    error = session.pop('login_error', None)
    return render_template('index.html', error=error)

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    asegurar_usuarios_en_sesion()
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()
        color = request.form.get('color', '#ffffff').strip()

        if not username or not password:
            flash("Debe ingresar nombre de usuario y contraseña.", "warning")
            return render_template('registro.html', username=username, color=color)

        usuarios = dict(session['usuarios'])
        if username in usuarios or username.lower() == 'admin':
            flash("El nombre de usuario ya existe o está reservado (admin).", "danger")
            return render_template('registro.html', username=username, color=color)

        usuarios[username] = {'password': password, 'color': color}
        session['usuarios'] = usuarios
        session.modified = True

        flash("Registro exitoso. Ahora inicie sesión.", "success")
        return redirect(url_for('index'))

    return render_template('registro.html')

@app.route('/login', methods=['POST'])
def login():
    asegurar_usuarios_en_sesion()
    username = request.form.get('username', '').strip()
    password = request.form.get('password', '').strip()

    if username == 'admin' and password == '12345678':
        session['usuario'] = 'admin'
        session['bgcolor'] = '#87CEEB'
        flash("Login correcto como admin.", "success")
        return redirect(url_for('inicio'))

    usuarios = session.get('usuarios', {})
    user = usuarios.get(username)

    if user and user.get('password') == password:
        session['usuario'] = username
        session['bgcolor'] = user.get('color', '#ffffff')
        flash(f"Login correcto. Bienvenido {escape(username)}.", "success")
        return redirect(url_for('inicio'))

    session['login_error'] = "Credenciales incorrectas. Intente de nuevo."
    return redirect(url_for('index'))

@app.route('/inicio')
def inicio():
    asegurar_usuarios_en_sesion()
    usuario = session.get('usuario')
    if not usuario:
        flash("Debe iniciar sesión primero.", "warning")
        return redirect(url_for('index'))

    bgcolor = session.get('bgcolor', '#ffffff')
    return render_template('inicio.html', usuario=usuario, bgcolor=bgcolor)

@app.route('/logout')
def logout():
    for key in ['usuario', 'bgcolor']:
        session.pop(key, None)
    flash("Sesión cerrada.", "info")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
