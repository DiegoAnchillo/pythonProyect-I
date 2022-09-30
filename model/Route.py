import random

class Route(object):
    
    def __init__(self, code: str, name: str, base_price: float,
                 economic: int, premium: int):
        
        self.code: str = code
        self.name: str = name
        self.base_price: float = base_price
        self.economic: int = economic
        self.premium: int = premium
        # Suma precio total a pagar (sin el IGV)
        self.total_price_economic: float = self.base_price + self.economic
        self.total_price_premium: float = self.base_price + self .premium

    def __repr__(self) -> str:
        """
        Método especial para representar el objeto de una clase como string.
        """
        return self.name

    """
        def __repr__(self) -> str:
        return f"{self.name}-{self.get_randon_sale_economic()}-{self.get_randon_sale_premiun()}"
    """
