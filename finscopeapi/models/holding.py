# finscopeapi/models/holding.py
from django.db import models

class Holding(models.Model):
    portfolio = models.ForeignKey('Portfolio', on_delete=models.CASCADE, related_name="holdings")
    ticker = models.CharField(max_length=20)
    quantity = models.DecimalField(max_digits=12, decimal_places=2)
    avg_purchase_price = models.DecimalField(max_digits=12, decimal_places=2)
    esg_company = models.ForeignKey('ESGCompany', on_delete=models.SET_NULL, null=True, blank=True, related_name="holdings")

    def __str__(self):
        return f"{self.ticker} ({self.portfolio.name})"
