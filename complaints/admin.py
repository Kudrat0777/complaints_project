from django.contrib import admin
from .models import Complaint, Response

admin.site.register(Complaint)
admin.site.register(Response)