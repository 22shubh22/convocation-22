from django.shortcuts import render
from . import forms
from . import models
# Create your views here.
def home_view(request):
    context = {}
    total_bid_on_shreya = sum(list(models.Bid.objects.filter(is_approved=True, vote="1").values_list("bid_amount", flat=True)))
    total_bid_on_shubham = sum(list(models.Bid.objects.filter(is_approved=True, vote="2").values_list("bid_amount", flat=True)))
    total_bid_on_raashid = sum(list(models.Bid.objects.filter(is_approved=True, vote="3").values_list("bid_amount", flat=True)))
    if request.method == 'POST':
        if "bid_create" in request.POST:
            bidcreateform = forms.BidCreateForm(request.POST)
            if bidcreateform.is_valid():
                bid = bidcreateform.save()
                bid.refresh_from_db()
                bid.save()
        if "do_calculation" in request.POST:
            calculation_form = forms.CalculationForm(request.POST)
            if calculation_form.is_valid():
                calculation_data = calculation_form.cleaned_data
                amount = calculation_data["amount"]
                etc_win_shreya = int((amount/(amount+total_bid_on_shreya)) * (total_bid_on_shubham + total_bid_on_raashid))
                etc_win_shubham = int((amount/(amount + total_bid_on_shubham)) * (total_bid_on_shreya + total_bid_on_raashid))
                etc_win_raashid = int((amount/(amount + total_bid_on_raashid)) * (total_bid_on_shreya + total_bid_on_shubham))
                context["calculation_value"] = True
                context["etc_win_shreya"] = etc_win_shreya
                context["etc_win_shubham"] = etc_win_shubham
                context["etc_win_raashid"] = etc_win_raashid
    context["bid_create_form"] = forms.BidCreateForm()
    context["calculation_form"] = forms.CalculationForm()
    context["shreya_supporters"] = models.Bid.objects.filter(vote="1")
    context["shubham_supporters"] = models.Bid.objects.filter(vote="2")
    context["rashid_supporters"] = models.Bid.objects.filter(vote="3")
    return render(request, "home.html", context)

def info_view(request):
    context = {}
    return render(request, "info.html", context)

def formula_view(request):
    context = {}
    return render(request, "formula.html", context)
