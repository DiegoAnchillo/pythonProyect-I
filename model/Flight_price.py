class Flight_price(object):

    def __init__(self, code_ruta:str,price_bs:float, economic_seat:float, premiun_seat:float):
        self.code_ruta:str = code_ruta,
        self.price_bs:float = price_bs,
        self.economic_seat:float = economic_seat,
        self.premiun_seat:float = premiun_seat

    def __repr__(self) -> str:
        return self.code_ruta