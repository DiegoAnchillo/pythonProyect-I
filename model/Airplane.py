
class Airplane(object):
    
    def __init__(self, name: str, n_seat: int):
        # Nombre del avion
        self.name: str = name
        # Numero asientos del avion
        self.n_seat:int = n_seat