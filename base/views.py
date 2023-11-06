from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Patient, TestRecords, MediaRecords, DiagnosticRecords, Prescription, TreatmentRecords, \
    ExerciseRecords, User
from .forms import PatientForm, DiagnosticRecordsForm, PrescriptionForm, TreatmentRecordsForm, ExerciseRecordsForm
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

def index(request):
    patient_list = Patient.objects.order_by('last_name', 'first_name')
    context = {'patient_list': patient_list}
    return render(request, 'base/patient_list.html', context)

def detail(request, Patient_id):
    patient = Patient.objects.get(id=Patient_id)
    context = {'patient' : patient}
    return render(request, 'base/patient_detail.html',context)

def create_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.save()
            return redirect('base:index')
    else:
        form = PatientForm()
    context = {'form': form}
    return render(request, 'base/patient_form.html', context)

class LoginAPIView(APIView):
    def post(self, request):
        user_id = request.data.get('user_id')
        password = request.data.get('password')
        user = authenticate(request, user_id=user_id, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)

def emr(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    # user = User.objects.get.all #의사와 환자 관계 재설정 필요
    test_records = TestRecords.objects.filter(patient=patient)
    media_records = MediaRecords.objects.filter(patient=patient)
    diagnostic_records = DiagnosticRecords.objects.filter(patient=patient)
    prescriptions = Prescription.objects.filter(patient=patient)
    treatment_records = TreatmentRecords.objects.filter(patient=patient)
    exercise_records = ExerciseRecords.objects.filter(patient=patient)

    context = {
        # 'user': user,
        'patient': patient,
        'test_records': test_records,
        'media_records': media_records,
        'diagnostic_records': diagnostic_records,
        'prescriptions': prescriptions,
        'treatment_records': treatment_records,
        'exercise_records': exercise_records,
    }

    # if request.method == "POST":
    #     diagnostic_form = DiagnosticRecordsForm(request.POST)
    #     prescription_form = PrescriptionForm(request.POST)
    #     treatment_form = TreatmentRecordsForm(request.POST)
    #     exercise_form = ExerciseRecordsForm(request.POST)
    #
    #
    # else:
    #     diagnostic_form = DiagnosticRecordsForm()
    #     prescription_form = PrescriptionForm()
    #     treatment_form = TreatmentRecordsForm()
    #     exercise_form = ExerciseRecordsForm()
    #
    # context = {
    #     'diagnostic_form': diagnostic_form,
    #     'prescription_form': prescription_form,
    #     'treatment_form': treatment_form,
    #     'exercise_form': exercise_form,
    # }
    return render(request, 'base/emr.html', context)

def recording(request,patient_id=None):
    patient = None
    if patient_id:
        patient = Patient.objects.get(id=patient_id)
    if request.method == "POST":
        diagnostic_form = DiagnosticRecordsForm(request.POST)
        prescription_form = PrescriptionForm(request.POST)
        treatment_form = TreatmentRecordsForm(request.POST)
        exercise_form = ExerciseRecordsForm(request.POST)

        # 폼 유효성 검사 및 저장 로직...

    else:
        diagnostic_form = DiagnosticRecordsForm()
        prescription_form = PrescriptionForm()
        treatment_form = TreatmentRecordsForm()
        exercise_form = ExerciseRecordsForm()

    context = {
        'diagnostic_form': diagnostic_form,
        'prescription_form': prescription_form,
        'treatment_form': treatment_form,
        'exercise_form': exercise_form,
    }

    return render(request, 'base/recording.html', context)