from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'zibcrm'

urlpatterns = [
    #ex: /crm/
    #path('', views.crm_page, name='club-home'), #simple data load and dump
    path('', views.show_with_json, name='club-home'), #json data load with data-table like show
    path('purchases', views.crm_json, name='club-json')
    
]