from django.shortcuts import render
from . import forms
# Create your views here.
def home_view(request):
    context = {}
    context["form"] = forms.BidCreateForm()
    return render(request, "home.html", context)
