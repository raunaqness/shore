from datetime import datetime, timedelta

from celery import shared_task
from celery.utils.log import get_task_logger

from shore_phase2.celery import app

from insights.models import UserInsightRecord
from insights.user_insights import UserInsights
from utils.email import send_email


logger = get_task_logger(__name__)

@shared_task
def send_user_insight_new_cheaper_product():
    """
    Send User Insight email if a 'new cheaper product is available' based on last 2 days of data
    """
    
    logger.info(f"Triggering Task : {send_user_insight_new_cheaper_product}")

    # try:
        # get time period
    end_date = datetime.now()
    start_date = end_date - timedelta(days=2)
    
    userinsights = UserInsights()
    userinsights.set_time_period(start_date=start_date, end_date=end_date)
    
    # check if cheaper product is available
    response = userinsights.check_if_cheaper_product_is_available()
    if response:
        user_email = response['user_email']
        send_email(email_to=user_email, 
                    email_subject="A cheaper product is available!", 
                    email_body=response['insight']
        )
        message = (f"Sent new user insights (cheaper product available) for user : {user_email}")
        
        # save insight to DB
        try:
            new_insight = UserInsightRecord(
                user_email=user_email,
                description=response['insight']
            )
            new_insight.save()
            logger.info("New UserInsightRecord created")
        except:
            logger.info("Failed to store new UserInsightRecord in DB.")
        
        logger.info(message)
        return message

    # except Exception as e:
        # logger.info("Exception occurred in 'product_search_email_every_x_mins'")
        
