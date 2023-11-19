from django.urls import path
from . import views
from .views import LoginAPIView
from .views import UserRegistrationAPIView
from .views import logout_view

app_name = 'base'

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:Patient_id>/', views.detail, name='detail'),
    path('create_patient/',views.create_patient,name='create_patient'),
    path('emr/<int:patient_id>/', views.emr, name='emr'),
    path('recording/<int:patient_id>/', views.recording, name='recording'),
    path('login/', LoginAPIView.as_view(), name='login'),
    # path('emr/<int:patient_id>/<int:user_id>/', views.emr, name='emr'),
    path('register/', UserRegistrationAPIView.as_view(), name='register'),
    path('logout/', logout_view, name='logout'),
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('appointments/create/', views.create_appointment, name='create_appointment'),
    path('update_appointment_status/<int:appointment_id>/', views.update_appointment_status,
         name='update_appointment_status'),
    path('appointments/complete/<int:appointment_id>/', views.complete_appointment, name='complete_appointment'),
]