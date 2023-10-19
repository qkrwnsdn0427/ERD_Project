from django import forms
from .models import Patient
from .models import DiagnosticRecords, Prescription,TreatmentRecords,ExerciseRecords
class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient  # 사용할 모델
        fields = ['last_name', 'first_name', 'birth_date', 'address', 'gender', 'phone_num', 'email', 'image']

class DiagnosticRecordsForm(forms.ModelForm):
    class Meta:
        model = DiagnosticRecords
        fields = ['symptoms', 'diagnosis', 'comments']

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['medicine', 'dosage', 'times', 'days', 'unit']

class TreatmentRecordsForm(forms.ModelForm):
    class Meta:
        model = TreatmentRecords
        fields = ['treatment_type', 'duration', 'time']

class ExerciseRecordsForm(forms.ModelForm):
    class Meta:
        model = ExerciseRecords
        fields = ['iteration', 'weight', 'duration', 'speed', 'distance', 'exercise_type']