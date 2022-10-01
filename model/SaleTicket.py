from config import IGV_PERCENT
from model.Route import Route
from typing import List

class SaleTicket(object):
    """
    Clase Boleto de viaje
    """
    def __init__(self, number: str, route: Route, typeTicket: str, subtotal:float):
        # Numero de ticket
        self.number: str = number
        # Ruta de viaje
        self.route: Route = route
        # Tipo de Boleto
        self.typeTicket: str = typeTicket
        # Subtotal del costo del Boleto
        self.subtotal: float = subtotal
        self.calculate_amounts()
    
    def calculate_amounts(self) -> None:
        # Calcula los montos que dependen del subtotal del Boleto
        self.igv: float = self.subtotal*IGV_PERCENT/100
        self.total: float = self.subtotal + self.igv