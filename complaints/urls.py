from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter
from .api import ComplaintViewSet, ResponseViewSet


router = DefaultRouter()
router.register(r'complaints', ComplaintViewSet)
router.register(r'responses', ResponseViewSet)

urlpatterns = [
    path('', views.complaint_list, name='complaint_list'),
    path('complaint/<int:pk>/', views.complaint_detail, name='complaint_detail'),
    path('api/', include(router.urls)),
]

