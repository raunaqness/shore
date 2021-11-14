import json
import requests
import random
from datetime import datetime, timedelta

from insights.constants import GET_PRODUCT_ALERT_RESPONSES_URL

class UserInsights:
    """Class Method to generate insights based on ProductAlertResults
    """
    
    def __init__(self):
        
        # init dates
        self.start_date = None
        self.end_date = None
        
        # store product results in variable in case
        # you want to run multiple business logics on the same data
        self.product_alert_results = None
        
    def set_time_period(self, start_date, end_date):
        """Set time period of data to be processed

        Args:
            start_date ([datetime]): start date
            end_date ([datetime]): end date
        """
        # number of days of data to be processed, default = '2'
        self.start_date = start_date
        self.end_date = end_date
        
        # reset product_alert_results
        self.product_alert_results = None 
        
    # for testing only
    def test_response(self):
        self.end_date = datetime.now()
        self.start_date = self.end_date - timedelta(2)
        
        self.get_product_results_data()
        return self.product_alert_results
    
        
    def get_product_results_data(self):
        """Helper function to fetch ProductAlertResults data
        """
        
        if (not self.start_date and self.end_date):
            return "Please set start_date and end_date by calling set_time_period()"
        
        try:
            url = f"{GET_PRODUCT_ALERT_RESPONSES_URL}?start_date={self.start_date}&end_date={self.end_date}"
            r = requests.get(url)
            json_response = json.loads(r.text)
            self.product_alert_results = json_response
            return True
            
        except Exception as e:
            print("Exception occured while fetching ProductResults data")
            print(f"message : {str(e)}")
            return False
            
        
    def check_if_cheaper_product_is_available(self):
        if not self.product_alert_results:
            success = self.get_product_results_data()
            if not success:
                print("Error occurred while fetch ProductAlertResults data")
                return None
        
        # TODO: complete business logic here
        # return sample response for now
        random_price = random.randint(129, 149)
        new_user_insight = f"""
                        A newer cheaper product is available for your search phrase : 'Intel'
                        Product name : Intel Core i7-6700K
                        Price: ${random_price}
        """
        
        # get user_email
        user_email = "raunaq@gmail.com"
        
        response = {
            "success": True,
            "insight" : new_user_insight,
            "user_email" : user_email
        }
        return response
        
        
        
            
        
        
            
        
        
            
        
        
    
    