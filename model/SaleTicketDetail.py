"""from config import PREMIUM_TYPE"""
from model.Route import Route


class SaleTicketDetail(object):
    def __init__(self, route: Route, quantity: int):
        """
        Constructor de la clase SaeTicketDetail
        """
        self.route: Route = route
        self.quantity: int = quantity
        """
        self.type: str = type
        self.total: float = round(self.calculateBasePrice() * quantity, 2)
        """

        """
        Obtener precio total del asiento economico y premium
        """
        self.total_economic: float = round(self.route.total_price_economic * self.quantity, 2)
        self.total_premium: float = round(self.route.total_price_premium * self.quantity, 2)

    """"
    nose que hace esta linea de codigo
    
    def calculateBasePrice(self):
        if(self.type is PREMIUM_TYPE):
            return self.route.base_price + self.route.premium
        return self.route.base_price + self.route.economic
    """
