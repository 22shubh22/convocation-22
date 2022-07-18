from django.db import models

# Create your models here.
class Bid(models.Model):
    bidder_name = models.CharField(max_length=200, null=True, blank=True)
    bid_amount = models.IntegerField(null=True, blank=True)
    choices = (("1", "shreya ananad"), ("2", "shubham upadhyay"), ("3", "rashid altaf"))
    vote = models.CharField(choices=choices, max_length=2, null=True, blank=True)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name + " (" + str(self.id) + ")"