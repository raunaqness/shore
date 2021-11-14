from django.db.models.base import Model
from rest_framework.serializers import ModelSerializer, ReadOnlyField

from alerts.models import ProductAlert, ProductAlertResult

class ProductAlertSerializer(ModelSerializer):
    user_email = ReadOnlyField(source='user.email')
    class Meta:
        model = ProductAlert
        fields = ('id', 'user_email', 'alert_frequency', 'product_search_phrase',
        'website')
        
class ProductAlertResultSerializer(ModelSerializer):
    class Meta:
        model = ProductAlertResult
        fields = '__all__'