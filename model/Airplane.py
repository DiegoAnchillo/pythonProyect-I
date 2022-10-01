
class Airplane(object):
    
    def __init__(self, name: str, n_seat: int, going: str, comeback: str):
        # Nombre del avion
        self.name: str = name
        # Numero asientos del avion
        self.n_seat: int = n_seat
        # Horario de salida
        self.going: str = going
        # Horario de regreso
        self.comeback: str = comeback