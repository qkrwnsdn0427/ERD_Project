from django.contrib import admin

# Register your models here.
from .models import Patient, User
from .models import DiagnosticRecords
from .models import TestRecords
from .models import MediaRecords
from .models import Prescription
from .models import TreatmentRecords
from .models import ExerciseRecords

admin.site.register(Patient)
admin.site.register(User)
admin.site.register(DiagnosticRecords)
admin.site.register(TestRecords)
admin.site.register(MediaRecords)
admin.site.register(Prescription)
admin.site.register(TreatmentRecords)
admin.site.register(ExerciseRecords)

