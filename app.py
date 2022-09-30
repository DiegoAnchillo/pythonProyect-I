from __future__ import annotations

from typing import List, Dict

from model.Airplane import Airplane
from model.Route import Route
from model.SaleTicket import SaleTicket
from model.SaleTicketDetail import SaleTicketDetail

def create_list_route() -> List[Route]:

    data_routes: List[Dict[str, str | float | int]] = [
        {
            "code": "LIM-AYA",
            "name": "LIMA-AYACUCHO",
            "base_price": 55.19,
            "economic": 8,
            "premium": 16,
            "min_sales_economic": 120,
            "max_sales_economic": 130,
            "min_sales_premium": 10,
            "max_sales_premium": 20
        },
        {
            "code": "LIM-CUS",
            "name": "LIMA-CUSCO",
            "base_price": 136.51,
            "economic": 8,
            "premium": 16,
            "min_sales_economic": 130,
            "max_sales_economic": 144,
            "min_sales_premium": 15,
            "max_sales_premium": 24
        },
        {
            "code": "LIM-ARE",
            "name": "LIMA-AREQUIPA",
            "base_price": 90.59,
            "economic": 8,
            "premium": 16,
            "min_sales_economic": 115,
            "max_sales_economic": 138,
            "min_sales_premium": 16,
            "max_sales_premium": 22
        },
        {
            "code": "LIM-TAR",
            "name": "LIMA-TARAPOTO",
            "base_price": 71.89,
            "economic": 8,
            "premium": 16,
            "min_sales_economic": 100,
            "max_sales_economic": 120,
            "min_sales_premium": 12,
            "max_sales_premium": 18
        },
        {
            "code": "AYA-LIM",
            "name": "AYACUCHO-LIMA",
            "base_price": 40.42,
            "economic": 7,
            "premium": 16,
            "min_sales_economic": 100,
            "max_sales_economic": 115,
            "min_sales_premium": 10,
            "max_sales_premium": 15
        },
        {
            "code": "CUS-LIM",
            "name": "CUSCO-LIMA",
            "base_price": 124.32,
            "economic": 7,
            "premium": 16,
            "min_sales_economic": 105,
            "max_sales_economic": 120,
            "min_sales_premium": 14,
            "max_sales_premium": 20
        },
        {
            "code": "ARE-LIM",
            "name": "AREQUIPA-LIMA",
            "base_price": 86.59,
            "economic": 7,
            "premium": 16,
            "min_sales_economic": 100,
            "max_sales_economic": 110,
            "min_sales_premium": 13,
            "max_sales_premium": 18
        },
        {
            "code": "TAR-LIM",
            "name": "TARAPOTO-LIMA",
            "base_price": 68.42,
            "economic": 7,
            "premium": 16,
            "min_sales_economic": 90,
            "max_sales_economic": 105,
            "min_sales_premium": 10,
            "max_sales_premium": 15
        }
    ]

    routes: List[Route] = []

    for key, route in enumerate(data_routes):
        obj_route = Route(str(route['code']), str(route['name']), float(route['base_price']), int(route['economic']),
                          int(route['premium']), int(route['min_sales_economic']), int(route['max_sales_economic']),
                          int(route['min_sales_premium']), int(route['max_sales_premium']))
        routes.append(obj_route)
    return routes



def create_list_airplane() -> List[Airplane]:

    data_plane: List[Dict[str, str | int]] = [
        {
            "name": "A001",
            "n_seat": 168
        },
        {
            "name": "A002",
            "n_seat": 168
        },
        {
            "name": "A003",
            "n_seat": 168
        },
        {
            "name": "A004",
            "n_seat": 168
        }
    ]

    airplanes: List[Airplane] = []

    for key, airplane in enumerate(data_plane):
        obj_airplane = Airplane(str(airplane['name']), int(airplane['n_seat']))
        airplanes.append(obj_airplane)
    return airplanes



def create_sales_ticket(route: Route, airplanes: List[Airplane]) -> List[SaleTicket]:

    list_tickets:List[SaleTicket] =[]

    sales_economic: int = route.get_randon_sale_economic()
    sales_premiun: int = route.get_randon_sale_premiun()

print(create_list_route())
create_list_airplane()