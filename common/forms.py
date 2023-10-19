
from base.models import User,DiagnosticRecords, Prescription,TreatmentRecords,ExerciseRecords
from django import forms
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    name = forms.CharField(max_length=50, label="이름")
    birth_date = forms.DateField(label="생년월일")
    address = forms.CharField(max_length=255, label="주소")
    gender = forms.ChoiceField(choices=User.GENDER_CHOICES, label="성별")
    phone_num = forms.CharField(max_length=15, label="전화번호")
    department = forms.CharField(max_length=50, label="부서", required=False)
    position = forms.CharField(max_length=50, label="직급", required=False)
    role = forms.ChoiceField(choices=User.ROLE_CHOICES, label="역할")
    password2 = forms.CharField(label="비밀번호 확인", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email", "name", "birth_date", "address", "gender", "phone_num", "department", "position", "role")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("비밀번호와 비밀번호 확인이 일치하지 않습니다.")

        return password2


