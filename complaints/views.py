from django.shortcuts import render
from .models import Complaint, Response


def complaint_list(request):
    complaints = Complaint.objects.all().order_by('-created_at')
    return render(request, 'templates/complaints/list.html', {'complaints': complaints})


def complaint_detail(request, pk):
    complaint = Complaint.objects.get(id=pk)
    responses = complaint.response_set.all()
    return render(request, 'templates/complaints/detail.html', {'complaint': complaint, 'responses': responses})
