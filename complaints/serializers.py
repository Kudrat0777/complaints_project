# complaints/serializers.py
from rest_framework import serializers
from .models import Complaint, Response

class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = ['external_id', 'user_id', 'text', 'status']


class ResponseSerializer(serializers.ModelSerializer):
    complaint_external_id = serializers.CharField(write_only=True)

    class Meta:
        model = Response
        fields = ['complaint', 'text', 'complaint_external_id']
        extra_kwargs = {'complaint': {'read_only': True}}

    def create(self, validated_data):
        complaint_external_id = validated_data.pop('complaint_external_id')
        complaint = Complaint.objects.get(external_id=complaint_external_id)
        validated_data['complaint'] = complaint
        return super().create(validated_data)
