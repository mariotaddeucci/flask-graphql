from . import db


class Department(db.Model):
    __tablename__ = 'department'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    employees = db.relationship('Employee')


class Employee(db.Model):
    __tablename__ = 'employee'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    hired_on = db.Column(db.DateTime)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))
    department = db.relationship('Department')
    tasks = db.relationship('Task')


class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column('id', db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
    title = db.Column(db.String(60))
    text = db.Column(db.String)
    done = db.Column(db.Boolean)
    pub_date = db.Column(db.DateTime)
    employee = db.relationship('Employee')
