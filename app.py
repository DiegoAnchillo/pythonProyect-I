from __future__ import annotations

from typing import List, Dict

from model.Airplane import Airplane
from model.Route import Route
from model.SaleTicket import SaleTicket
from config import CURRENCY_SYMBOL
import utils


def create_list_routes() -> List[Route]:
    # Función que crea y devuelve una lista de objetos Route
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

    # print(data_routes)

    routes: List[Route] = []

    for key, route in enumerate(data_routes):
        obj_route = Route(str(route['code']), str(route['name']), float(route['base_price']), int(route['economic']),
                          int(route['premium']), int(route['min_sales_economic']), int(route['max_sales_economic']),
                          int(route['min_sales_premium']), int(route['max_sales_premium']))
        routes.append(obj_route)
    return routes



def create_list_airplanes() -> List[Airplane]:
    # Función que crea y devuelve una lista de objetos Airplane
    data_plane: List[Dict[str, str | int]] = [
        {
            "name": "A001",
            "n_seat": 168,
            "going": "06:30 AM",
            "comeback": "15:45 PM"
        },
        {
            "name": "A002",
            "n_seat": 168,
            "going": "07:25 AM",
            "comeback": "16:25 PM"
        },
        {
            "name": "A003",
            "n_seat": 168,
            "going": "08:10 AM",
            "comeback": "17:15 PM"
        },
        {
            "name": "A004",
            "n_seat": 168,
            "going": "08:50 AM",
            "comeback": "17:50 PM"
        }
    ]

    # print(data_plane)

    airplanes: List[Airplane] = []

    for key, airplane in enumerate(data_plane):
        obj_airplane = Airplane(str(airplane['name']), int(airplane['n_seat']),
                                str(airplane['going']), str(['comeback']))
        airplanes.append(obj_airplane)
    return airplanes


def create_sales_tickets(route: Route) -> List[SaleTicket]:

    list_tickets: List[SaleTicket] = []
    
    # Obtenemos la cantidad de ventas de asiento economico de manera aleatoria
    sales_economic: int = route.get_randon_sale_economic()
    # Obtenemos la cantidad de ventas de asiento premium de manera aleatoria
    sales_premiun: int = route.get_randon_sale_premiun()
    
    for i in range(sales_economic):
        # list_tickets: List[SaleTicketDetail] = create_detail_sale_ticket(airplane, route)
        # sale_ticket: SaleTicket = SaleTicket(airplane, list_tickets)
        # list_tickets.append(sale_ticket)
        correlative: str = str(i+1).zfill(5)
        ticket_number: str = f"{route.code}{correlative}"
        subtotal: float = round(route.base_price + route.economic, 2)

        # Creamos el objeto SaleTicket
        sale_ticket: SaleTicket = SaleTicket(ticket_number, route, "Economic", subtotal)

        # Agregamos el objeto Saleticket en una lista
        list_tickets.append(sale_ticket)
        
    for i in range(sales_premiun):
        # list_tickets: List[SaleTicketDetail] = create_detail_sale_ticket(airplane, route)
        # sale_ticket: SaleTicket = SaleTicket(airplane, list_tickets)
        # list_tickets.append(sale_ticket)
        correlative: str = str(i+1).zfill(5)
        ticket_number: str = f"{route.code}{correlative}"
        subtotal: float = round(route.base_price + route.premium, 2)

        # Creamos el objeto SaleTicket
        sale_ticket: SaleTicket = SaleTicket(ticket_number, route, "Premium", subtotal)

        # Agregamos el objeto Saleticket en una lista
        list_tickets.append(sale_ticket)    
        
    return list_tickets


def main():
    # Función principal del módulo app.py

    # Crear la lista de objetos Route
    routes: List[Route] = create_list_routes()

    # Crear la lista de objetos Airplane
    airplanes: List[Airplane] = create_list_airplanes()

    print("\n")
    print("*"*30)
    print("REPORTE DE VENTAS DEL DIA")
    print("*"*30)
    print("\n")
    
    t_total_sales: int = 0
    t_economic_sales: float = 0
    t_premium_sales: float = 0

    for key, route in enumerate(routes):
        # creamos la lista de objetos SaleTicket (tickets de venta)
        list_sales_tickets: List[SaleTicket] = create_sales_tickets(route)

        # Total de tickets de venta
        total_sales = len(list_sales_tickets)
        t_total_sales += total_sales
        
        # Total de ingresos por Boletos Economicos
        economic_sales: float = round(
            sum([ticket.total for k, ticket in enumerate(list_sales_tickets) if ticket.typeTicket == "Economic"]), 2)
        t_economic_sales += economic_sales

        # Total de ingresos por Boletos Economicos
        premiun_sales: float = round(
            sum([ticket.total for k, ticket in enumerate(list_sales_tickets) if ticket.typeTicket == "Premium"]), 2)
        t_premium_sales += premiun_sales

        # Calcular la suma total de ventas
        rep_total_sale = round(
            sum([ticket.total for k, ticket in enumerate(list_sales_tickets)]), 2)

        # Calculando la suma total de IGV cobrado
        rep_total_igv: float = round(
            sum([ticket.igv for k, ticket in enumerate(list_sales_tickets)]), 2)

        # Calculando el valor del ticket promedio de venta.
        ticket_avg: float = round(rep_total_sale / total_sales, 2)

        # Ordenemos lista de tickets (de menor a mayor)
        sorted_tickets: List[SaleTicket] = sorted(
            list_sales_tickets, key=lambda x: x.total)

        # Obtenemos la cantidad de tickets cuyo importe supera el ticket promedio
        rep_tickets_higher_than: int = len(
            [k for k, ticket in enumerate(sorted_tickets) if ticket.total > ticket_avg])


        # Mostramos en pantalla valores calculados.
        print(f"Ruta: {route.name}")
        print(f"Cod. Ruta: {route.code}")
        print(f"Ventas: {total_sales}")
        print(
            f"Total de Ventas: {utils.get_currency_format(CURRENCY_SYMBOL,rep_total_sale)}")
        
        print(
            f"Total de Ventas Boletos economico: {utils.get_currency_format(CURRENCY_SYMBOL,economic_sales)}")

        print(
            f"Total de Ventas Boletos premium: {utils.get_currency_format(CURRENCY_SYMBOL, premiun_sales)}")

        print(
            f"Total de IGV: {utils.get_currency_format(CURRENCY_SYMBOL, rep_total_igv)}")
        print(
            f"Ticket Promedio: {utils.get_currency_format(CURRENCY_SYMBOL, ticket_avg)}")
        print(
            f"Ticket de Venta más baja: {utils.get_currency_format(CURRENCY_SYMBOL, sorted_tickets[0].total)}")
        print(
            f"Ticket de Venta más alta: {utils.get_currency_format(CURRENCY_SYMBOL, sorted_tickets[-1].total)}")
        print(
            f"Total de Tickets mayor al promedio de venta: {rep_tickets_higher_than}")
        print("\n")
        print("-"*30)
        print("\n")

        
        
    print(f"Total de pasajes vendidos : {t_total_sales}")
    print(
          f"Total de Boletos Economicos: {utils.get_currency_format(CURRENCY_SYMBOL, t_economic_sales)}")
    print(
        f"Total de Boletos Premium: {utils.get_currency_format(CURRENCY_SYMBOL, t_premium_sales)}")
    
    print("\n")
    print("-"*30)
    print("\n")


if __name__ == "__main__":
    main()
