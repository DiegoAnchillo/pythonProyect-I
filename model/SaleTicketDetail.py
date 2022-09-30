from config import PREMIUM_TYPE
from model.Route import Route

class SaleTicketDetail(object):
    def __init__(self, route: Route, quantity:int, type: str):
        self.route: Route = route
        self.quantity: int = quantity
        self.type: str = type
        self.total: float = round(self.calculateBasePrice() * quantity,2)
    
    def calculateBasePrice(self):
        if(self.type is PREMIUM_TYPE):
            return self.route.base_price + self.route.premium
        return self.route.base_price + self.route.economic