from django.contrib import admin
from . import models
# Register your models here.
class BidAdmin(admin.ModelAdmin):
    model = models.Bid
    list_display = ["id", "bidder_name", "bid_amount", "is_approved"]
    search_fields = ["name"]

admin.site.register(models.Bid, BidAdmin)