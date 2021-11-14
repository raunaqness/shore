from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from alerts.views import *

urlpatterns = [
    
    # internal endpoints
    path('get_product_alerts', ProductAlertListView.as_view()),
    path('create_product_alert', create_product_alert, name="create_product_alert"),
    path('get_product_alert_details/<int:id>', get_product_alert_details, name="get_product_alert_details"),
    path('get_all_product_alert_results', ProductAlertResultListView.as_view()),
        
    # get product alert responses between start_date and end_date
    path('get_product_alert_responses', get_product_alert_responses, name="get_product_alert_responses")
]