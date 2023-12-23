from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from .models import Patient, MedicalRecord
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    patients = Patient.query.filter_by(doctor_id=current_user.id).all()
    return render_template('profile.html', name=current_user.name, patients=patients)

@main.route('/patient/<int:id>')
@login_required
def patient(id):
    medical_records = MedicalRecord.query.filter_by(patient_id=id).all()
    return render_template('patient.html', patient=Patient.query.get_or_404(id), medical_records=medical_records)

@main.route('/add_medical_record', methods=['POST'])
@login_required
def add_medical_record():
    diagnosis = request.form.get('diagnosis')
    prescription = request.form.get('prescription')
    treatment_plan = request.form.get('treatment_plan')
    patient_id = request.form.get('patient_id')

    if(prescription == ''):
        import pytholog as pl
        from .logic import pr_kb
        prescription = pr_kb.query(pl.Expr(f'prescription_for({diagnosis.lower().replace(" ", "_")}, What)'))[0]['What']
        prescription = prescription.replace("_", " ").capitalize()
    
    if(treatment_plan == ''):
        import pytholog as pl
        from .logic import tr_kb
        treatment_plan = tr_kb.query(pl.Expr(f'treatment_plan_for({diagnosis.lower().replace(" ", "_")}, What)'))[0]['What']
        treatment_plan = treatment_plan.replace("_", " ").capitalize()


    if(treatment_plan == ''):
        treatment_plan = None

    medical_record = MedicalRecord(
        diagnosis=diagnosis, 
        patient_id=patient_id, 
        prescription=prescription, 
        treatment_plan=treatment_plan
    )

    db.session.add(medical_record)
    db.session.commit()
    flash('Medical record added')
    
    return redirect(url_for('main.patient', id=patient_id))

@main.route('/delete_patient/<int:id>')
@login_required
def delete_patient(id):
    patient = Patient.query.get_or_404(id)
    db.session.delete(patient)
    db.session.commit()
    flash('Patient deleted')
    return redirect(url_for('main.profile'))

@main.route('/delete_medical_record/<int:id>')
@login_required
def delete_medical_record(id):
    medical_record = MedicalRecord.query.get_or_404(id)
    db.session.delete(medical_record)
    db.session.commit()
    flash('Medical record deleted')
    return redirect(url_for('main.patient', id=medical_record.patient_id))

@main.route('/add_patient', methods=['POST'])
@login_required
def add_patient():
    name = request.form.get('name')
    gender = request.form.get('gender')
    phone = request.form.get('phone')
    address = request.form.get('address')
    admission_date = request.form.get('admission_date')
    discharge_date = request.form.get('discharge_date')
    patient = Patient(
        name=name, 
        gender=gender, 
        phone=phone, 
        address=address,
        admission_date=admission_date,
        discharge_date=discharge_date,
        doctor_id=current_user.id
    )

    db.session.add(patient)
    db.session.commit()
    flash('Patient added')
    return redirect(f'/patient/{patient.id}')