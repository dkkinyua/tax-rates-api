from django.urls import path
from core import views

urlpatterns = [
    path('taxrates/', views.get_tax_rates, name='get-tax-rates'),
]