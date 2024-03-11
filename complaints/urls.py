from django.urls import path
from . import views

urlpatterns = [
    path('', views.complaint_list, name='complaint_list'),
    path('complaint/<int:pk>/', views.complaint_detail, name='complaint_detail'),
]
