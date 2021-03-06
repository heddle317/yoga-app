import json

from app import app
from app.db.asanas import Asana
from app.db.user import get_verified_user
from app.utils.decorators.template_globals import use_template_globals

from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask_login import login_required
from flask_login import login_user
from flask_login import logout_user


@app.route('/admin')
@login_required
@use_template_globals
def admin():
    g.nav_view = 'admin'
    return render_template('admin.html')


@app.route('/login', methods=['GET'])
@use_template_globals
def login_template():
    return render_template('login.html')


@app.route('/login', methods=["POST"])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    user = get_verified_user(email, password)
    if user:
        login_user(user, remember=True)
        return redirect('/admin/asana')
    return redirect('/login')


@app.route('/logout', methods=["GET"])
@login_required
def logout():
    logout_user()
    return redirect('/login')


@app.route('/admin/asana', methods=['GET'])
@login_required
@use_template_globals
def get_asanas():
    if request.is_xhr:
        asanas = Asana.get_asanas()
        return json.dumps(asanas), 200, {'Content-Type': 'application/json'}
    g.nav_view = 'asana'
    return render_template('edit_asanas.html')
