# complaints/api.py
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ResponseSerializer
from .models import Complaint


class ResponseAPIView(APIView):
    def post(self, request, format=None):
        serializer = ResponseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CheckComplaintAPIView(APIView):
    def post(self, request, format=None):
        user_id = request.data.get('user_id')
        external_id = request.data.get('external_id')
        # Проверяем, существует ли жалоба
        complaint, created = Complaint.objects.get_or_create(
            external_id=external_id, 
            defaults={'user_id': user_id}
            )
        if created:
            # Жалоба была создана
            return Response({'status': 'created', 'external_id': external_id}, status=status.HTTP_201_CREATED)
        else:
            # Жалоба уже существовала
            return Response({'status': 'exists', 'external_id': external_id}, status=status.HTTP_200_OK)