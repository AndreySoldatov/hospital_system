# models.py

from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    medical_record_id = db.Column(db.Integer, db.ForeignKey('medical_record.id'))
    doctor_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    name = db.Column(db.String(100))
    gender = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    address = db.Column(db.String(100))

    admission_date = db.Column(db.String(100))
    discharge_date = db.Column(db.String(100))

class MedicalRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))

    diagnosis = db.Column(db.String(100))
    prescription = db.Column(db.String(100))

    treatment_plan = db.Column(db.String(100))