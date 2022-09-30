import random

class Route(object):
    
    def __init__(self, code: str, name: str, base_price: float,
                 economic: int, premium: int,
                 min_sales_economic: int, max_sales_economic: int,
                 min_sales_premium: int, max_sales_premium):
        # Codigo de la ruta
        self.code: str = code
        # Nombre de la ruta
        self.name: str = name
        # Precio base del costo de Boleto
        self.base_price: float = base_price
        # Precio adicional del Boleto economico
        self.economic: int = economic
        # Precio adicional del Boleto premium
        self.premium: int = premium
        # Ventas minimas de Boleto economico
        self.min_sales_economic: int = min_sales_economic
        # Ventas maximas de Boleto economico
        self.max_sales_economic: int = max_sales_economic
        # Ventas minimas de Boleto premium
        self.min_sales_premium: int = min_sales_premium
        # Ventas maximas de Boleto premium
        self.max_sales_premium: int = max_sales_premium

    def __repr__(self) -> str:
        # Método especial para representar el objeto de una clase como string.
        return self.name

    def get_randon_sale_economic(self) -> int:
        """
        Devuelve un número de ventas de Boleto economico de manera aleatoria 
        basada en el rango de ventas mínimas y máximas.
        """
        return random.randint(self.min_sales_economic, self.max_sales_economic)

    def get_randon_sale_premiun(self) -> int:
        """
        Devuelve un número de ventas de Boleto premium de manera aleatoria 
        basada en el rango de ventas mínimas y máximas.
        """
        return random.randint(self.min_sales_premium, self.max_sales_premium)
