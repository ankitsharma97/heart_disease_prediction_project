# prediction_app/urls.py
from django.urls import path
from .views import predict_heart_disease,index

urlpatterns = [
    path('predict/', predict_heart_disease, name='predict_heart_disease'),
    path('', index, name='index'),
]
