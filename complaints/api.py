# complaints/api.py
from rest_framework import viewsets
from .models import Complaint, Response
from .serializers import ComplaintSerializer, ResponseSerializer

class ComplaintViewSet(viewsets.ModelViewSet):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer

class ResponseViewSet(viewsets.ModelViewSet):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer
