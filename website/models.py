from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField(blank=True)
    message = models.CharField(max_length=2000)
 
    def __str__(self):
        return f"{self.name}, {self.email}"


class Benchmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type_analysis = models.CharField(max_length=256)
    country = models.CharField(max_length=256)
    industry = models.CharField(max_length=256)
    credit_rating_borrower = models.CharField(max_length=256)
    currency = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    type_of_interest_rate = models.CharField(max_length=256)
    base_rate = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.type_analysis}, {self.country}"



