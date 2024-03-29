from django.db import models

# Create your models here.
class Bid(models.Model):
    bidder_name = models.CharField(max_length=200)
    bid_amount = models.IntegerField()
    choices = (("1", "Shreya Ananad"), ("2", "Shubham Upadhyay"), ("3", "Raashid Altaf"))
    vote = models.CharField(choices=choices, max_length=2)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)