from django.core.checks.messages import Error
from alerts.models import ProductAlertResult

def create_product_alert_results(productalert_id, response):
    """
    Utility function to create ProductAlertResult record
    """

    try:
        product_alert_result = ProductAlertResult()
        product_alert_result.product_alert_id = productalert_id
        product_alert_result.response = response

        product_alert_result.save()

    except Exception as e:
        print("Error occurred while saving ProductAlertResult record.")