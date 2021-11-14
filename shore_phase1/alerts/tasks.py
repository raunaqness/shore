from typing import ItemsView
from celery import shared_task
from celery.app import task
from celery.utils.log import get_task_logger

from shore_phase1.celery import app

from alerts.models import ProductAlert
from alerts.utils import create_product_alert_results
from utils.ebay.ebay_api import EbayAPI
from utils.email import send_email


logger = get_task_logger(__name__)

@shared_task
def sample_task():
    logger.info("The sample task just ran.")

@shared_task
def product_search_email_every_x_mins(alert_frequency, website):
    """
    Send Product search Alerts every 'alert_frequency' minutes
    """
    
    logger.info(f"Triggering Task : {product_search_email_every_x_mins}")
    logger.info(f"alert_frequency : {alert_frequency} | website : {website}")

    try:
        # get product alert records
        queryset = ProductAlert.objects.filter(
            alert_frequency=alert_frequency,
            website=website
        ).values(
            'id', 'user__email', 'product_search_phrase'
        )

        logger.info(f"queryset : {queryset}")
        for record in queryset:
            create_product_search_alert_ebay.delay(record['id'], record['user__email'], record['product_search_phrase'])

    except Exception as e:
        logger.info("Exception occurred in 'product_search_email_every_x_mins'")

@app.task(name="create_product_search_alert_ebay")
def create_product_search_alert_ebay(productalert_id, user_email, product_search_phrase):
    """
    
    """
    logger.info(f"Executing Product Search for Ebay with phrase : {product_search_phrase}")
    try:
        api = EbayAPI()
        response = api.search_keywords(product_search_phrase)

        logger.info(f"{len(response)} items received in response for search phrase : {product_search_phrase}")
        logger.info("Sending email to : {user_email}")
        send_email(
            email_to=user_email, 
            email_subject="Your Search Alert from EBAY", 
            email_body="HTML Containing Products and prices"
        )

        # save to DB
        logger.info("Saving results to DB.")
        create_product_alert_results(productalert_id, response)

    except Exception as e:
        logger.info("Failed while executing task.")
        




