# import form class from django
from django import forms
  
# import GeeksModel from models.py
from .models import Bid
  
# create a ModelForm
class BidCreateForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Bid
        fields = ("bidder_name", "bid_amount", "vote")

class CalculationForm(forms.Form):
    amount = forms.IntegerField(label="Amount")