
class Report(object):
    
    def __init__(self, code_route: str, n_seat_sales: int, 
                 n_seat_economic: int, 
                 n_seat_premium: int, 
                 t_economic_sales: float,
                 t_premium_sales: float,
                 t_igv_sales: float,
                 t_total_sales: float,
                 name_airplane: str):
        # Codigo de la ruta
        self.code_route: str = code_route
        # Numero asientos vendidos
        self.n_seat_sales: int = n_seat_sales
        # Numero asientos Economicos vendidos
        self.n_seat_economic: int = n_seat_economic
        # Numero asientos Premium vendidos
        self.n_seat_premium: int = n_seat_premium
        # Total de Ventas de boletos Economicos
        self.t_economic_sales: float = t_economic_sales
        # Total de Ventas de boletos Premium
        self.t_premium_sales: float = t_premium_sales
        # Total de Igv
        self.t_igv_sales: float = t_igv_sales
        # Total de Ventas de la ruta
        self.t_total_sales: float = t_total_sales
        # Avion asignado a la ruta
        self.name_airplane: str = name_airplane
        