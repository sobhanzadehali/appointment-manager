from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import os
from models import db, Patient, Doctor, Appointment

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointments.db'
db.init_app(app)

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

# Patient routes
@app.route('/patients')
def patients():
    patients = Patient.query.all()
    return render_template('patients.html', patients=patients)

@app.route('/patients/new', methods=['GET', 'POST'])
def new_patient():
    if request.method == 'POST':
        try:
            patient = Patient(
                name=request.form.get('name'),
                email=request.form.get('email'),
                phone=request.form.get('phone')
            )
            db.session.add(patient)
            db.session.commit()
            flash('Patient added successfully!', 'success')
            return redirect(url_for('patients'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding patient: {str(e)}', 'error')
            return redirect(url_for('new_patient'))
    return render_template('new_patient.html')

@app.route('/patients/<int:patient_id>/edit', methods=['GET', 'POST'])
def edit_patient(patient_id):
    patient = Patient.query.get_or_404(patient_id)
    if request.method == 'POST':
        try:
            patient.name = request.form.get('name')
            patient.email = request.form.get('email')
            patient.phone = request.form.get('phone')
            db.session.commit()
            flash('Patient updated successfully!', 'success')
            return redirect(url_for('patients'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating patient: {str(e)}', 'error')
            return redirect(url_for('edit_patient', patient_id=patient_id))
    return render_template('edit_patient.html', patient=patient)

@app.route('/patients/<int:patient_id>/delete', methods=['POST'])
def delete_patient(patient_id):
    try:
        patient = Patient.query.get_or_404(patient_id)
        # Check if patient has appointments
        if patient.appointments:
            flash('Cannot delete patient with existing appointments!', 'error')
            return redirect(url_for('patients'))
        
        db.session.delete(patient)
        db.session.commit()
        flash('Patient deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting patient: {str(e)}', 'error')
    return redirect(url_for('patients'))

# Doctor routes
@app.route('/doctors')
def doctors():
    doctors = Doctor.query.all()
    return render_template('doctors.html', doctors=doctors)

@app.route('/doctors/new', methods=['GET', 'POST'])
def new_doctor():
    if request.method == 'POST':
        try:
            doctor = Doctor(
                name=request.form.get('name'),
                specialization=request.form.get('specialization'),
                email=request.form.get('email'),
                phone=request.form.get('phone')
            )
            db.session.add(doctor)
            db.session.commit()
            flash('Doctor added successfully!', 'success')
            return redirect(url_for('doctors'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding doctor: {str(e)}', 'error')
            return redirect(url_for('new_doctor'))
    return render_template('new_doctor.html')

@app.route('/doctors/<int:doctor_id>/edit', methods=['GET', 'POST'])
def edit_doctor(doctor_id):
    doctor = Doctor.query.get_or_404(doctor_id)
    if request.method == 'POST':
        try:
            doctor.name = request.form.get('name')
            doctor.specialization = request.form.get('specialization')
            doctor.email = request.form.get('email')
            doctor.phone = request.form.get('phone')
            db.session.commit()
            flash('Doctor updated successfully!', 'success')
            return redirect(url_for('doctors'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating doctor: {str(e)}', 'error')
            return redirect(url_for('edit_doctor', doctor_id=doctor_id))
    return render_template('edit_doctor.html', doctor=doctor)

@app.route('/doctors/<int:doctor_id>/delete', methods=['POST'])
def delete_doctor(doctor_id):
    try:
        doctor = Doctor.query.get_or_404(doctor_id)
        # Check if doctor has appointments
        if doctor.appointments:
            flash('Cannot delete doctor with existing appointments!', 'error')
            return redirect(url_for('doctors'))
        
        db.session.delete(doctor)
        db.session.commit()
        flash('Doctor deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting doctor: {str(e)}', 'error')
    return redirect(url_for('doctors'))

@app.route('/appointments')
def appointments():
    appointments = Appointment.query.order_by(Appointment.date, Appointment.time).all()
    return render_template('appointments.html', appointments=appointments)

@app.route('/appointments/new', methods=['GET', 'POST'])
def new_appointment():
    if request.method == 'POST':
        try:
            # Get form data
            patient_id = request.form.get('patient')
            doctor_id = request.form.get('doctor')
            date_str = request.form.get('date')
            time_str = request.form.get('time')
            notes = request.form.get('notes')

            # Convert date and time strings to datetime objects
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
            time = datetime.strptime(time_str, '%H:%M').time()

            # Create new appointment
            appointment = Appointment(
                patient_id=patient_id,
                doctor_id=doctor_id,
                date=date,
                time=time,
                notes=notes
            )

            # Save to database
            db.session.add(appointment)
            db.session.commit()

            flash('Appointment created successfully!', 'success')
            return redirect(url_for('appointments'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error creating appointment: {str(e)}', 'error')
            return redirect(url_for('new_appointment'))

    # For GET request, fetch patients and doctors for the form
    patients = Patient.query.all()
    doctors = Doctor.query.all()
    return render_template('new_appointment.html', patients=patients, doctors=doctors)

@app.route('/appointments/<int:appointment_id>/delete', methods=['POST'])
def delete_appointment(appointment_id):
    try:
        appointment = Appointment.query.get_or_404(appointment_id)
        db.session.delete(appointment)
        db.session.commit()
        flash('Appointment deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting appointment: {str(e)}', 'error')
    return redirect(url_for('appointments'))

if __name__ == '__main__':
    app.run(debug=True)


