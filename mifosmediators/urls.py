"""
django_openhim_mediators URL Configuration for MIFOS endpoints
"""
from django.contrib import admin
from django.urls import path

from patient_mediator.views import getClient
from patient_mediator.views import registerClientMediator


urlpatterns = [
    path('admin/', admin.site.urls),
    path('fineract-provider/api/v1/clients', getClient),

]

""" 
Register Mediators - once -- uncomment after setting up variables
The function throws invalid Url; to check after setting variables
"""

# registerClientMediator()