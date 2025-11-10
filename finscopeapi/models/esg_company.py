# finscopeapi/models/esg_company.py
from django.db import models

class ESGCompany(models.Model):
    ticker = models.CharField(max_length=20, unique=True)
    company_name = models.CharField(max_length=255)
    sector = models.CharField(max_length=100)
    esg_score = models.IntegerField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.company_name} ({self.ticker})"
