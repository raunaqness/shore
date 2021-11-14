from django.db import models
from enum import Enum
from django.contrib.auth.models import User


class Website(Enum):
    EBAY = ('EBAY', 'EBay')
    AMAZON = ('AMAZON', 'Amazon')


# Create your models here.
class ProductAlert(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    alert_frequency = models.IntegerField(
        # add index?
        blank=False,
        null=False,
        default=2,
        help_text="Frequency in minutes at which alert will be triggered"
    )
    product_search_phrase = models.CharField(
        blank=False,
        null=False,
        max_length=50,
        help_text="Search term for which user wants product results"
    )
    website = models.CharField(
        null=False,
        blank=False,
        max_length=20,
        choices=[x.value for x in Website],
        default=Website.EBAY.value
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateField(
        auto_now_add=True
    )

    def __str__(self):
        return self.product_search_phrase



    
class ProductAlertResult(models.Model):
    product_alert = models.ForeignKey(
        ProductAlert,
        on_delete=models.DO_NOTHING
    )
    response = models.JSONField(
        help_text="Response received from the server"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return str(self.product_alert)


