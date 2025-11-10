# finscopeapi/models/portfolio.py
from django.db import models
from django.contrib.auth.models import User

class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="portfolios")
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    total_value = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.name} ({self.user.username})"
