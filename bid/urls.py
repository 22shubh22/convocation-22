from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home_view, name="home_view"),
    path('croods/', views.info_view, name = "croods"),
    path('formula/', views.formula_view, name = "formula"),
]