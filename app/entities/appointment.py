from entities.patient import Patient
from entities.doctor import Doctor
from datetime import datetime

class Appointment:
    def __init__(self, patient: Patient, doctor: Doctor, date: datetime, time: datetime):
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time
    
    def __str__(self):
        return f"Appointment(patient={self.patient}, doctor={self.doctor}, date={self.date}, time={self.time})"
    
    def __repr__(self):
        return f"Appointment(patient={self.patient}, doctor={self.doctor}, date={self.date}, time={self.time})"
    
    

