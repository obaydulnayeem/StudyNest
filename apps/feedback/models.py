from django.db import models
from django.contrib.auth.models import User

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    love_count = models.PositiveIntegerField(default=0)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Feedback by {self.user.username} on {self.created_at}"