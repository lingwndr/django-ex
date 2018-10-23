from django.shortcuts import render
from django.http import HttpResponse
from .models import Purchase, Customer
from django.template import loader
from django.shortcuts import render
from django.core import serializers

def crm_page(request):
    query_result = None
    if not request.user.is_superuser:
        try:
            customer = Customer.objects.get(national_id=request.user.username)
            query_result = Purchase.objects.filter(buyer=customer)
        except (Purchase.DoesNotExist, Customer.DoesNotExist) as e:
            pass
    else:
        query_result = Purchase.objects.all()
    context = {
        'user_purchase_list': query_result,
    }
    return render(request, 'zibcrm/club.html', context)

def crm_json(request):
    query_result = None
    try:
        customer = Customer.objects.get(national_id=request.user.username)
        query_result = Purchase.objects.filter(buyer=customer)
    except (Purchase.DoesNotExist, Customer.DoesNotExist) as e:
        query_result = ''

    json = serializers.serialize('json', query_result, use_natural_foreign_keys=True)
    return HttpResponse(json, content_type='application/json')
    
def show_with_json(request):
    return render(request, 'zibcrm/club-json.html')