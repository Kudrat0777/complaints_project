from django.db import models


class Complaint(models.Model):
    external_id = models.CharField(max_length=100, unique=True)
    user_id = models.CharField(max_length=100)
    text = models.TextField(blank=True)  # Позволим тексту быть пустым, так как изначально текст может не быть предоставлен
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, default='new')

    def __str__(self):
        # Возвращаем идентификатор и первые 50 символов текста для удобства
        return f"{self.external_id} - {self.user_id[:50]}..."

class Response(models.Model):
    complaint = models.ForeignKey(Complaint, related_name='responses', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Возвращаем первые 50 символов текста ответа для удобства
        return f"{self.text[:50]}..."
