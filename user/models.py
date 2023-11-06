from django.db import models

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
