from django.db import models

# Create your models here.

class Log(models.Model):
    customer_name = models.CharField(max_length=30)
    customer_email = models.CharField(max_length=30)
    status = models.CharField(max_length=10)
    transaction_type = models.CharField(max_length=20)
    narration = models.CharField(max_length=50)
    account = models.CharField(max_length=10)
    amount = models.IntegerField()
    currency = models.CharField(max_length=3)
    transaction_ref = models.CharField(max_length=35)
    flw_ref = models.CharField(max_length=35)
    created_at = models.CharField(max_length=26)

    def __str__(self):
        return self.transaction_type
