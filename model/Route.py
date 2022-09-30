import random


class Route(object):
    
    def __init__(self, code: str, name: str, base_price: float,
                 economic: int, premium: int,
                 min_sales_economic: int, max_sales_economic: int,
                 min_sales_premium: int, max_sales_premium):
        
        self.code: str = code
        self.name: str = name
        self.base_price: float = base_price
        self.economic: int = economic
        self.premium: int = premium
        self.min_sales_economic: int = min_sales_economic
        self.max_sales_economic: int = max_sales_economic
        self.min_sales_premium: int = min_sales_premium
        self.max_sales_premium: int = max_sales_premium

    def __repr__(self) -> str:
        return f"{self.name}-{self.get_randon_sale_economic()}-{self.get_randon_sale_premiun()}"

    def get_randon_sale_economic(self) -> int:
        return random.randint(self.min_sales_economic, self.max_sales_economic)

    def get_randon_sale_premiun(self) -> int:
        return random.randint(self.min_sales_premium, self.max_sales_premium)
