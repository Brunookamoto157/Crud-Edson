from app import db


class Department(db.Model):
    __tablename__ = 'departments'
    id = db.Column(db.Integer, primary_key=True)
    building = db.Column(db.String(100))
    budget = db.Column(db.Float(precision=2))


class Studant(db.Model):
    __tablename__ = 'studants'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    tot_cred = db.Column(db.Integer)
    fk_department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))

    department = db.relationship(Department, backref='studants')