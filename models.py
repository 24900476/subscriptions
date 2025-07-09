from django.db import models
from django.contrib.auth.models import User

class Subscription(models.Model):
    PLAN_CHOICES = [
        ('free', 'Free'),
        ('basic', 'Basic'),
        ('premium', 'Premium'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='subscription')
    plan = models.CharField(max_length=10, choices=PLAN_CHOICES, default='free')
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - {self.get_plan_display()}"
