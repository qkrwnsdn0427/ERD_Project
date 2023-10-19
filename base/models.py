from django.db import models
from django.contrib.auth.models import AbstractUser

# Patient 모델 정의
class Patient(models.Model):
    id = models.AutoField(primary_key=True)  # id 필드를 다시 추가
    last_name = models.CharField(max_length=50, null=False)
    first_name = models.CharField(max_length=50, null=False)
    birth_date = models.DateField(null=False)
    address = models.CharField(max_length=255, null=False)
    GENDER_CHOICES = [
        ('M', '남성'),
        ('F', '여성'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=False)
    phone_num = models.CharField(max_length=15, null=False)
    email = models.CharField(max_length=100, null=True)
    image = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.first_name

# User 모델 정의
class User(models.Model):
    id = models.AutoField(primary_key=True)  # id 필드를 다시 추가
    user_id = models.CharField(max_length=15, null=False)
    user_pw = models.CharField(max_length=100, null=False)
    name = models.CharField(max_length=50, null=False)
    birth_date = models.DateField(null=False)
    address = models.CharField(max_length=255, null=False)
    GENDER_CHOICES = [
        ('M', '남성'),
        ('F', '여성'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=False)
    phone_num = models.CharField(max_length=15, null=False)
    email = models.CharField(max_length=100, null=True)
    department = models.CharField(max_length=50, null=True)
    position = models.CharField(max_length=50, null=True)
    ROLE_CHOICES = [
        ('관리자', '관리자'),
        ('의사', '의사'),
        ('물리 치료사', '물리 치료사'),
        ('기타 의료진', '기타 의료진'),
        ('환자', '환자'),
        ('간호사', '간호사'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, null=False)

    def __str__(self):
        return self.user_id

class TestRecords(models.Model):
    test_code = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING, null=True, blank=True)
    MuscleMass = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    BodyFatMass = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    Muscular_strength = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    cardio_endurance = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    agility = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    flexibility = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    #data_code = models.AutoField()
    date = models.DateField()

    def __str__(self):
        return f" 신체계측/바이탈 "

class MediaRecords(models.Model):
    data_code = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING, null=True, blank=True)
    TestRecords.test_code = models.ForeignKey(TestRecords, on_delete=models.DO_NOTHING, related_name='media', null=True, blank=True)
    inbody_url = models.CharField(max_length=255, null=True, blank=True)
    video_url = models.CharField(max_length=255, null=True, blank=True)
    xray_url = models.CharField(max_length=255, null=True, blank=True)
    Field4 = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f" 매체 자료 "

class DiagnosticRecords(models.Model):
    diagnosis_code = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    diagnosis_date = models.DateField(auto_now_add=True)
    symptoms = models.CharField(max_length=55,null=True, blank=True)
    diagnosis = models.CharField(max_length=55, null=True, blank=True)
    comments = models.CharField(max_length=55, null=True, blank=True)
    prescription_code = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return f"진료기록"

class Prescription(models.Model):
    prescription_code = models.AutoField(primary_key=True)
    DiagnosticRecords.diagnosis_code = models.ForeignKey(DiagnosticRecords, on_delete=models.DO_NOTHING, related_name='처방', null=True, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING, related_name='처방', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='처방', null=True, blank=True)
    medicine = models.CharField(max_length=15, null=True, blank=True)
    dosage = models.IntegerField( null=True, blank=True)
    times = models.IntegerField( null=True, blank=True)
    days = models.IntegerField( null=True, blank=True)
    unit = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return f" 처방 "
class TreatmentRecords(models.Model):
    treatment_code = models.AutoField(primary_key=True)
    DiagnosticRecords.diagnosis_code = models.ForeignKey(DiagnosticRecords, on_delete=models.DO_NOTHING, related_name='치료', null=True, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING, related_name='치료', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='치료', null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    treatment_type = models.CharField(max_length=30, null=True, blank=True)
    duration = models.IntegerField( null=True, blank=True)
    time = models.IntegerField( null=True, blank=True)

    def __str__(self):
        return f" 치료 "
class ExerciseRecords(models.Model):
    EXERCISE_TYPE_CHOICES = [
        ('strength', '무산소'),
        ('cardio', '유산소'),
    ]

    exercise_code = models.AutoField(primary_key=True)
    DiagnosticRecords.diagnosis_code = models.ForeignKey(DiagnosticRecords, on_delete=models.DO_NOTHING, related_name='운동', null=True, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING, related_name='운동', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='운동', null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    iteration = models.IntegerField( null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    duration = models.IntegerField( null=True, blank=True)
    speed = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    distance = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    exercise_type = models.CharField(max_length=10, choices=EXERCISE_TYPE_CHOICES, null=True, blank=True)

    def __str__(self):
        return f" 운동 "
