from django.shortcuts import render
from . import forms
from . import models
# Create your views here.
def home_view(request):
    if request.method == 'POST':
        bidcreateform = forms.BidCreateForm(request.POST)
        if bidcreateform.is_valid():
            bid = bidcreateform.save()
            bid.refresh_from_db()
            bid.save()
    context = {}
    context["form"] = forms.BidCreateForm()
    context["shreya_supporters"] = models.Bid.objects.filter(vote="1")
    context["shubham_supporters"] = models.Bid.objects.filter(vote="2")
    context["rashid_supporters"] = models.Bid.objects.filter(vote="3")
    return render(request, "home.html", context)

def info_view(request):
    context = {}
    return render(request, "info.html", context)
