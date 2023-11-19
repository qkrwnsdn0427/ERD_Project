from django import forms
from .models import Patient, Appointments
from .models import DiagnosticRecords, Prescription, TreatmentRecords, ExerciseRecords, User
import datetime


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


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_id', 'name', 'birth_date', 'address', 'gender', 'phone_num', 'email', 'password', 'department',
                  'position', 'role']


# views.py
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # 사용자 생성 로직 추가
            form.save()  # UserRegistrationForm이 ModelForm을 상속받고 있다고 가정
            # 폼 데이터 처리
            return redirect('somewhere')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


class AppointmentForm(forms.ModelForm):
    appointment_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    appointment_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time', 'min': '09:00', 'max': '18:50', 'step': 600}))

    class Meta:
        model = Appointments
        fields = ['doctor', 'patient', 'appointment_date', 'appointment_time', 'symptoms', 'purpose']

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        # '의사' 역할을 가진 사용자만을 대상으로 의사 필드의 쿼리셋을 필터링합니다.
        self.fields['doctor'].queryset = User.objects.filter(role='의사')
