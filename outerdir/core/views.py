import os
import json

from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings

from rest_framework.decorators import api_view
from django_ratelimit.decorators import ratelimit

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

@ratelimit(key='ip', rate='20/m', block=True)
@api_view(['GET'])
def get_tax_rates(request):

    with open("core/data/tax.json", 'r') as f:
        data = json.load(f)

    return JsonResponse(data)