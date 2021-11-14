import json
from dateutil.parser import parse as dateutil_parse
import pdb

from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from django.contrib.auth.models import User
from django.views.generic import ListView

from alerts.models import *
from alerts.serializers import *
from alerts.forms import *

from alerts.constants import product_alerts_view_filters


@api_view(['GET'])
def index(request):
    return Response("success")

class ProductAlertListView(ListView):
    queryset = ProductAlert.objects.order_by('-created_at')
    template_name = "alerts/productalert_list.html"

class ProductAlertResultListView(ListView):
    queryset = ProductAlertResult.objects.order_by('-created_at')
    template_name = "alerts/productalertresult_list.html"


@api_view(['GET', 'POST'])
def create_product_alert(request):
    """Create new ProductAlerts

    Args:
        request ([type]): [description]

    Returns:
        [type]: [description]
    """
    if request.method == "POST":
        form = ProductAlertForm(data=request.data)
        if form.is_valid():
            form.save()
            context = {
                "form": form,
                "message": "Product Alert Created!"
            }
            return render(request, 'forms/create_product_alert_form.html', context)
        else:
            context = {
                "message": "Failed"
            }
            return render(request, 'forms/create_product_alert_form.html', context)
        
    else:
        form = ProductAlertForm
        return render(request, 'forms/create_product_alert_form.html', {'form': form})
    
    
@api_view(["GET"])
def get_product_alert_details(request, id):
    """[summary]

    Args:
        request ([type]): [description]

    Returns:
        [type]: [description]
    """
    
    # try:
    product_alert = ProductAlert.objects.filter(id=id).first()
    serializer = ProductAlertSerializer(product_alert)
    response = {
        "data" : serializer.data
    }
    return Response(response, status=200)

    # except:
        # return Response({"message" : "Not Found."}, status=200)
    
        

@api_view(['GET'])
def get_product_alert_responses(request):
    """Get All ProductAlertResults between start_date and end_date

    Args:
        request ([type]): [description]

    Returns:
        [type]: [description]
    """
    
    try:
        start_date = dateutil_parse(request.query_params['start_date'])
        end_date = dateutil_parse(request.query_params['end_date'])
        
        filter_dict = {
            "created_at__gte" : start_date,
            "create_at__lte" : end_date
        }
        
        queryset = ProductAlertResult.objects.filter(
            created_at__gte=start_date,
            created_at__lte=end_date
        )   
        
        serializer = ProductAlertResultSerializer(queryset, many=True)
        response = {
            "data" : serializer.data
        }
        
        return Response(response)
        
    except:
        return Response({"message" : "Please pass valid start_date and end_date as query params."})
    