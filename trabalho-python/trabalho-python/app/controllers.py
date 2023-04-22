from flask import Blueprint, jsonify, request
from app import db
from app.models import Department, Studant

api = Blueprint('api', __name__)

@api.route('/departments', methods=['GET'])
def get_departments():
    departments = Department.query.all()
    return jsonify([department.serialize() for department in departments]), 200

@api.route('/studants', methods=['GET'])
def get_studants():
    studants = Studant.query.all()
    return jsonify([studant.serialize() for studant in studants]), 200

@api.route('/studants', methods=['POST'])
def create_studant():
    name = request.json.get('name')
    tot_cred = request.json.get('tot_cred')
    department_id = request.json.get('department_id')

    department = Department.query.get(department_id)
    if not department:
        return jsonify({'error': 'Department not found.'}), 404

    studant = Studant(name=name, tot_cred=tot_cred, department=department)
    db.session.add(studant)
    db.session.commit()

    return jsonify(studant.serialize()), 201
