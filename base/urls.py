from django.urls import path
from . import views
from .views import LoginAPIView

app_name = 'base'

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:Patient_id>/', views.detail, name='detail'),
    path('create_patient/',views.create_patient,name='create_patient'),
    path('emr/<int:patient_id>/', views.emr, name='emr'),
    path('recording/<int:patient_id>/', views.recording, name='recording'),
    path('login/', LoginAPIView.as_view(), name='login'),
    # path('emr/<int:patient_id>/<int:user_id>/', views.emr, name='emr'),
]