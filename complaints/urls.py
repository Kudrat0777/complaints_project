from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter
from .api import ResponseAPIView, CheckComplaintAPIView


router = DefaultRouter()

urlpatterns = [
    path('', views.complaint_list, name='complaint_list'),
    path('complaint/<int:pk>/', views.complaint_detail, name='complaint_detail'),
    path('api/responses/', ResponseAPIView.as_view()),
    path('api/check_complaint/', CheckComplaintAPIView.as_view()),
]

