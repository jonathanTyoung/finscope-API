# finscopeapi/models/transaction.py
from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ("BUY", "Buy"),
        ("SELL", "Sell"),
        ("DEPOSIT", "Deposit"),
        ("WITHDRAW", "Withdraw")
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="transactions")
    portfolio = models.ForeignKey('Portfolio', on_delete=models.CASCADE, related_name="transactions")
    ticker = models.CharField(max_length=20)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    quantity = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    price_per_share = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_type} {self.ticker} ({self.user.username})"
