# finscopeapi/models/report.py
from django.db import models
from django.contrib.auth.models import User

class Report(models.Model):
    REPORT_TYPES = [
        ("performance", "Performance"),
        ("risk", "Risk"),
        ("ESG", "ESG")
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reports")
    portfolio = models.ForeignKey('Portfolio', on_delete=models.CASCADE, related_name="reports")
    report_type = models.CharField(max_length=20, choices=REPORT_TYPES)
    file_path = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.report_type} report ({self.portfolio.name})"
