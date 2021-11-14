from ebay_rest import API, DateTime, Error, Reference


class EbayAPI():

    def __init__(self):
        self.api = None
        self.initialize_api()
    
    def initialize_api(self):
        try:
            self.api = API(application='production_1', user='production_1', header='US')
        except Error as error:
            print(f"Error occured while initializing Ebay API.")
            print(f'Error {error.number} is {error.reason}  {error.detail}.\n')

    def search_keywords(self, query, sort='price', limit=20):
        """
        Search Ebay with query, and some optional parameters

        Input:
            query (str) : search query
            sort (str): sort by type, default = 'price' (optional)
            limit (int): max number of results to return, default = '20' (optional)

        Output:
            items (list[dict]) : records as dict
        """

        try:
            response = self.api.buy_browse_search(q='iphone', sort='price', limit=20)
            
            items = []
            for item in response:
                record = item.get('record', None)
                if record: items.append(record)
            
            return items

        except Error as error:
            print(f"Error occured while using 'search keywords' API.")
            print(f'Error {error.number} is {error.reason}  {error.detail}.\n')


