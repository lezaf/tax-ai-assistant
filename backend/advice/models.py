from django.db import models

class ChatHistory(models.Model):
    user_id = models.CharField(max_length=255, unique=True)
    messages = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)