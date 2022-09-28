
class Airplane(object):
    
    def __init__(self, name: str, n_seatings: int, state: bool):
        
        self.name: str = name
        self.n_seating:int = n_seatings
        self.state: bool = state