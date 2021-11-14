from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer

# Create your views here.
from django.views.generic import ListView
from insights.models import UserInsightRecord
from insights.tasks import send_user_insight_new_cheaper_product

class UserInsightRecordListView(ListView):
    queryset = UserInsightRecord.objects.order_by('-created_at')
    template_name = "insights/userinsightrecord_list.html"
    
@api_view(["GET"])
def run_generate_user_insight_task(request):
    """Temp function to manually run UserInsight Generation task

    Args:
        request ([type]): [description]
    """
    # import pdb
    # pdb.set_trace()
    res = send_user_insight_new_cheaper_product()
    return redirect('/insights/')
    # return render_template('insights/userinsightrecord_list.html')
    
    
    
    
    