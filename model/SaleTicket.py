
from config import IGV_PERCENT
from model.Airplane import Airplane
from model.SaleTicketDetail import SaleTicketDetail
from typing import List


class SaleTicket(object):
    def __init__(self, number: str, airplane: Airplane, list_detail: List[SaleTicketDetail]):
        self.number: str = number
        self.airplane: Airplane = airplane
        self.list_detail: List[SaleTicketDetail] = list_detail

    def __repr__(self) -> str:
        return self.number
    
    def calculate_amounts(self):
        self.subtotal = sum([detail.total for key, detail in enumerate(self.list_detail)])
        self.igv: float = self.subtotal * IGV_PERCENT/100
        self.total: float = self.subtotal + self.igv
    
    