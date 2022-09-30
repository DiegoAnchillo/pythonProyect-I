import random


class Airplane(object):
    
    def __init__(self, name: str, n_seat: int, route_going: str, route_comeback: str,
                 hour_going: str, hour_comeback: str,
                 min_sales_economic_going: int, max_sales_economic_going: int,
                 min_sales_premium_going: int, max_sales_premium_going: int,
                 min_sales_economic_comeback: int, max_sales_economic_comeback: int,
                 min_sales_premium_comeback: int, max_sales_premium_comeback: int,
                 ):
        # Nombre del avion
        self.name: str = name
        # Numero asientos del avion
        self.n_seat: int = n_seat
        # Nombre de la ruta de ida y vuelta
        self.route_going: str = route_going
        self.route_comeback: str = route_comeback
        # Horario de la ruta de ida y vuelta
        self.hour_going: str = hour_going
        self.hour_going: str = hour_comeback
        # Ruta de ida - precio economico y premium
        self.min_sales_economic_going: int = min_sales_economic_going
        self.max_sales_economic_going: int = max_sales_economic_going
        self.min_sales_premium_going: int = min_sales_premium_going
        self.max_sales_premium_going: int = max_sales_premium_going
        # Ruta de vuelta - precio economico y premium
        self.min_sales_economic_comeback: int = min_sales_economic_comeback
        self.max_sales_economic_comeback: int = max_sales_economic_comeback
        self.min_sales_premium_comeback: int = min_sales_premium_comeback
        self.max_sales_premium_comeback: int = max_sales_premium_comeback

    def __repr__(self) -> str:
        """
        Método especial para representar el objeto de una clase como string.
        """
        return self.name

    def get_randon_sale_economic_going(self) -> int:
        """
        Generador random del asiento economico ida
        """
        return random.randint(self.min_sales_economic_going, self.max_sales_economic_going)

    def get_randon_sale_premiun_going(self) -> int:
        """
        Generador random del asiento premium ida
        """
        return random.randint(self.min_sales_premium_going, self.max_sales_premium_going)

    def get_randon_sale_economic_comeback(self) -> int:
        """
        Generador random del asiento economico vuelta
        """
        return random.randint(self.min_sales_economic_comeback, self.max_sales_economic_comeback)

    def get_randon_sale_premiun_comeback(self) -> int:
        """
        Generador random del asiento premium vuelta
        """
        return random.randint(self.min_sales_premium_comeback, self.max_sales_premium_comeback)
