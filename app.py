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
            "premium": 16
        },
        {
            "code": "LIM-CUS",
            "name": "LIMA-CUSCO",
            "base_price": 136.51,
            "economic": 8,
            "premium": 16
        },
        {
            "code": "LIM-ARE",
            "name": "LIMA-AREQUIPA",
            "base_price": 90.59,
            "economic": 8,
            "premium": 16
        },
        {
            "code": "LIM-TAR",
            "name": "LIMA-TARAPOTO",
            "base_price": 71.89,
            "economic": 8,
            "premium": 16
        },
        {
            "code": "AYA-LIM",
            "name": "AYACUCHO-LIMA",
            "base_price": 40.42,
            "economic": 7,
            "premium": 16
        },
        {
            "code": "CUS-LIM",
            "name": "CUSCO-LIMA",
            "base_price": 124.32,
            "economic": 7,
            "premium": 16
        },
        {
            "code": "ARE-LIM",
            "name": "AREQUIPA-LIMA",
            "base_price": 86.59,
            "economic": 7,
            "premium": 16
        },
        {
            "code": "TAR-LIM",
            "name": "TARAPOTO-LIMA",
            "base_price": 68.42,
            "economic": 7,
            "premium": 16
        }
    ]

    routes: List[Route] = []

    for key, route in enumerate(data_routes):
        obj_route = Route(str(route['code']), str(route['name']), float(route['base_price']), int(route['economic']),
                          int(route['premium']))
        routes.append(obj_route)
    return routes


def create_list_airplane() -> List[Airplane]:

    data_plane: List[Dict[str, str | int]] = [
        {
            "name": "A001",
            "n_seat": 168,
            "route_going": "LIMA-AYACUCHO",
            "route_comeback": "AYACUCHO-LIMA",
            "hour_going": "06:30 AM",
            "hour_comeback": "15:45 PM",
            "min_sales_economic_going": 120,
            "max_sales_economic_going": 130,
            "min_sales_premium_going": 10,
            "max_sales_premium_going": 20,
            "min_sales_economic_comeback": 100,
            "max_sales_economic_comeback": 115,
            "min_sales_premium_comeback": 10,
            "max_sales_premium_comeback": 15

        },
        {
            "name": "A002",
            "n_seat": 168,
            "route_going": "LIMA-CUSCO",
            "route_comeback": "CUSCO-LIMA",
            "hour_going": "07:25 AM",
            "hour_comeback": "16:25 PM",
            "min_sales_economic_going": 130,
            "max_sales_economic_going": 144,
            "min_sales_premium_going": 15,
            "max_sales_premium_going": 24,
            "min_sales_economic_comeback": 105,
            "max_sales_economic_comeback": 120,
            "min_sales_premium_comeback": 14,
            "max_sales_premium_comeback": 20
        },
        {
            "name": "A003",
            "n_seat": 168,
            "route_going": "LIMA-AREQUIPA",
            "route_comeback": "AREQUIPA-LIMA",
            "hour_going": "08:10 AM",
            "hour_comeback": "17:15 PM",
            "min_sales_economic_going": 115,
            "max_sales_economic_going": 138,
            "min_sales_premium_going": 16,
            "max_sales_premium_going": 22,
            "min_sales_economic_comeback": 100,
            "max_sales_economic_comeback": 110,
            "min_sales_premium_comeback": 13,
            "max_sales_premium_comeback": 18
        },
        {
            "name": "A004",
            "n_seat": 168,
            "route_going": "LIMA-TARAPOTO",
            "route_comeback": "TARAPOTO-LIMA",
            "hour_going": "08:50 AM",
            "hour_comeback": "17:50 PM",
            "min_sales_economic_going": 100,
            "max_sales_economic_going": 110,
            "min_sales_premium_going": 12,
            "max_sales_premium_going": 18,
            "min_sales_economic_comeback": 90,
            "max_sales_economic_comeback": 105,
            "min_sales_premium_comeback": 10,
            "max_sales_premium_comeback": 15
        }
    ]

    airplanes: List[Airplane] = []

    for key, airplane in enumerate(data_plane):
        obj_airplane = Airplane(str(airplane['name']), int(airplane['n_seat']),
                                str(airplane['route_going']), str(airplane['route_comeback']),
                                str(['hour_going']), str(['hour_comeback']),
                                int(airplane['min_sales_economic_going']),
                                int(airplane['max_sales_economic_going']),
                                int(airplane['min_sales_premium_going']),
                                int(airplane['max_sales_premium_going']),
                                int(airplane['min_sales_economic_comeback']),
                                int(airplane['max_sales_economic_comeback']),
                                int(airplane['min_sales_premium_comeback']),
                                int(airplane['max_sales_premium_comeback']))
        airplanes.append(obj_airplane)
    return airplanes


def create_sales_ticket(airplane: Airplane, route: List[Route]) -> List[SaleTicket]:

    list_tickets: List[SaleTicket] = []

    sales_economic: int = route.get_randon_sale_economic()
    sales_premiun: int = route.get_randon_sale_premiun()

    for i in range(sales_economic):
        list_tickets: List[SaleTicketDetail] = create_detail_sale_ticket(airplane, route)

        sale_ticket: SaleTicket = SaleTicket(airplane, list_tickets)
        list_tickets.append(sale_ticket)
    return list_tickets

def create_detail_sale_ticket(airplane, route):
    pass


create_list_route()

create_list_airplane()
