from django.db import models


class Complaint(models.Model):
    user_id = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, default='new')

    def __str__(self):
        return f"{self.text[:50]}..."


class Response(models.Model):
    complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text[:50]}..."
