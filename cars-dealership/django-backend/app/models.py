from django.db import models
from django.contrib.auth.models import User

class Dealer(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    address = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.city}, {self.state})"

class Review(models.Model):
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    rating = models.IntegerField(default=5)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
