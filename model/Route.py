
from xmlrpc.client import boolean


class Route(object):
    
    def __init__(self, code: str, name: str, base_price: float, 
                 economic: float, premium: float, 
                 min_sales_economic: float, max_sales_economic: float,
                 min_sales_premium: float, max_sales_premium: float, 
                 state: bool, airplane_code: str):
        
        self.code: str = code
        self.name: str = name
        self.base_price: float = base_price
        self.economic: float = economic
        self.premium: float = premium
        self.min_sales_economic: float = min_sales_economic
        self.max_sales_economic: float = max_sales_economic
        self.min_sales_premium: float = min_sales_premium
        self.max_sales_premium: float = max_sales_premium
        self.state: bool = state
        self.airplane_code: str = airplane_code