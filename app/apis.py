import json

from app import app
from app.db.asanas import Asana

# from flask import g
# from flask import redirect
from flask import flash
from flask import request
from flask_login import login_required


@app.route('/admin/asana', methods=['POST'])
@login_required
def create_asana():
    data = json.loads(request.data)
    try:
        asana = Asana.create_asana(**data)
    except ValueError as e:
        flash(e.message, 'danger')
        return json.dumps({'message': e.message}), 400, {'Content-Type': 'application/json'}
    return json.dumps(asana), 200, {'Content-Type': 'application/json'}


@app.route('/admin/asana/<uuid>', methods=['PUT'])
@login_required
def edit_asana(uuid):
    asana = Asana.update_asana(uuid, **request.form)
    return json.dumps(asana), 200, {'Content-Type': 'application/json'}


@app.route('/admin/asana/<uuid>', methods=['DELETE'])
@login_required
def delete_asana(uuid):
    Asana.delete_asana(uuid)
    return json.dumps({'message': 'Your asana was successfully deleted.'}), 200, {'Content-Type': 'application/json'}
