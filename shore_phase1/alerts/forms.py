from django.forms import ModelForm
from alerts.models import ProductAlert

class ProductAlertForm(ModelForm):
    class Meta:
        model = ProductAlert
        fields = "__all__"