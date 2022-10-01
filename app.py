from __future__ import annotations

from typing import List, Dict

from model.Airplane import Airplane
from model.Report import Report
from model.Route import Route
from model.SaleTicket import SaleTicket
from config import CURRENCY_SYMBOL
import utils


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
    
    airplanes: List[Airplane] = []

    for key, airplane in enumerate(data_plane):
        obj_airplane = Airplane(str(airplane['name']), int(airplane['n_seat']),
                                str(airplane['going']), str(['comeback']))
        airplanes.append(obj_airplane)
    return airplanes


def create_list_routes() -> List[Route]:
    # Crear la lista de objetos Airplane
    airplanes: List[Airplane] = create_list_airplanes()

    # Función que crea y devuelve una lista de objetos Route
    data_routes: List[Dict[str, str | float | int | Airplane]] = [
        {
            "code": "LIM-AYA",
            "name": "LIMA-AYACUCHO",
            "base_price": 55.19,
            "economic": 8,
            "premium": 16,
            "min_sales_economic": 120,
            "max_sales_economic": 130,
            "min_sales_premium": 10,
            "max_sales_premium": 20,
            "plane": Airplane(airplanes[0].name, airplanes[0].n_seat, airplanes[0].going, airplanes[0].comeback)
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
            "max_sales_premium": 24,
            "plane": Airplane(airplanes[1].name, airplanes[1].n_seat, airplanes[1].going, airplanes[1].comeback)
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
            "max_sales_premium": 22,
            "plane": Airplane(airplanes[2].name, airplanes[2].n_seat, airplanes[2].going, airplanes[2].comeback)
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
            "max_sales_premium": 18,
            "plane": Airplane(airplanes[3].name, airplanes[3].n_seat, airplanes[3].going, airplanes[3].comeback)
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
            "max_sales_premium": 15,
            "plane": Airplane(airplanes[0].name, airplanes[0].n_seat, airplanes[0].going, airplanes[0].comeback)
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
            "max_sales_premium": 20,
            "plane": Airplane(airplanes[1].name, airplanes[1].n_seat, airplanes[1].going, airplanes[1].comeback)
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
            "max_sales_premium": 18,
            "plane": Airplane(airplanes[2].name, airplanes[2].n_seat, airplanes[2].going, airplanes[2].comeback)
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
            "max_sales_premium": 15,
            "plane": Airplane(airplanes[3].name, airplanes[3].n_seat, airplanes[3].going, airplanes[3].comeback)
        }
    ]

    routes: List[Route] = []

    for key, route in enumerate(data_routes):
        obj_route = Route(str(route['code']), str(route['name']), float(route['base_price']), int(route['economic']),
                          int(route['premium']), int(route['min_sales_economic']), int(route['max_sales_economic']),
                          int(route['min_sales_premium']), int(route['max_sales_premium']), 
                          Airplane(route['plane'].name, route['plane'].n_seat,
                                   route['plane'].going, route['plane'].comeback))
        routes.append(obj_route)
    return routes


def create_sales_tickets(route: Route) -> List[SaleTicket]:

    list_tickets: List[SaleTicket] = []
    
    # Obtenemos la cantidad de ventas de asiento economico de manera aleatoria
    sales_economic: int = route.get_randon_sale_economic()
    # Obtenemos la cantidad de ventas de asiento premium de manera aleatoria
    sales_premiun: int = route.get_randon_sale_premiun()
    
    for i in range(sales_economic):
        correlative: str = str(i+1).zfill(5)
        ticket_number: str = f"{route.code}{correlative}"
        subtotal: float = round(route.base_price + route.economic, 2)

        # Creamos el objeto SaleTicket
        sale_ticket: SaleTicket = SaleTicket(ticket_number, route, "Economic", subtotal)

        # Agregamos el objeto Saleticket en una lista
        list_tickets.append(sale_ticket)
        
    for i in range(sales_premiun):
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

    list_report: List[Report] = []
    
    for key, route in enumerate(routes):
        # creamos la lista de objetos SaleTicket (tickets de venta)
        list_sales_tickets: List[SaleTicket] = create_sales_tickets(route)

        # Total de tickets de venta
        seat_sales = len(list_sales_tickets)

        # Obteniendo numero Boletos Economicos.
        n_economic: int = len(
            [k for k, ticket in enumerate(list_sales_tickets) if ticket.typeTicket == "Economic"])
        
        # Obteniendo numero Boletos Premium.
        n_premium: int = len([k for k, ticket in enumerate(list_sales_tickets) if ticket.typeTicket == "Premium"])
        
        # Total de ingresos por Boletos Economicos
        economic_sales: float = round(
            sum([ticket.total for k, ticket in enumerate(list_sales_tickets) if ticket.typeTicket == "Economic"]), 2)
        
        # Total de ingresos por Boletos Premium
        premiun_sales: float = round(
            sum([ticket.total for k, ticket in enumerate(list_sales_tickets) if ticket.typeTicket == "Premium"]), 2)
        
        # Calculando la suma total de IGV cobrado
        total_igv: float = round(
            sum([ticket.igv for k, ticket in enumerate(list_sales_tickets)]), 2)
        
        # Calcular la suma total de ventas
        total_sale = round(
            sum([ticket.total for k, ticket in enumerate(list_sales_tickets)]), 2)
        
        # Guardando nuestro objeto Report
        obj_report = Report(route.code, seat_sales, n_economic, n_premium,
                            economic_sales, premiun_sales, total_igv, total_sale, route.airplane.name)
        
        list_report.append(obj_report)
        
    # Total de tickets de venta
    seat_sales: int = sum(
        [report.n_seat_sales for k, report in enumerate(list_report)])
    
    # Total de ingresos por Boletos Economicos
    economic_sales: float = sum(
        [report.t_economic_sales for k, report in enumerate(list_report)])
    
    # Total de ingresos por Boletos Premium
    premium_sales: float = sum(
        [report.t_premium_sales for k, report in enumerate(list_report)])
    
    # Obteniendo numero Boletos Economicos.
    n_economic: int = sum(
        [report.n_seat_economic for k, report in enumerate(list_report)])
    
    # Obteniendo numero Boletos Premium.
    n_premium: int = sum(
        [report.n_seat_premium for k, report in enumerate(list_report)])
    
    # Calculando la suma total de IGV cobrado
    total_igv: float = sum(
        [report.t_igv_sales for k, report in enumerate(list_report)])
    
    # Ordenemos lista de Report (de menor a mayor segun cantidad de pasajeros)
    sorted_reports_seat: List[Report] = sorted(
        list_report, key=lambda x: x.n_seat_sales)
    
    # Ordenemos lista de Report (de menor a mayor segun cantidad de pasajeros)
    sorted_reports_sale: List[Report] = sorted(
        list_report, key=lambda x: x.t_total_sales)
    
    print("\n")
    print("*"*30)
    print("REPORTE DE VENTAS DEL DIA")
    print("*"*30)
    print("\n")
    print(f"Total de pasajes vendidos : {seat_sales}")
    print(
        f"Total Ingresos por venta Boletos Economicos: {utils.get_currency_format(CURRENCY_SYMBOL, economic_sales)}")
    print(
        f"Total Ingresos por venta Boletos Premium: {utils.get_currency_format(CURRENCY_SYMBOL, premium_sales)}")
    print(
        f"Total de IGV: {utils.get_currency_format(CURRENCY_SYMBOL, total_igv)}")
    print(
        f"Valor Promedio Pasaje Economico: "
        f"{utils.get_currency_format(CURRENCY_SYMBOL, round(economic_sales / n_economic, 2))}")
    print(
        f"Valor Promedio Pasaje Premium: "
        f"{utils.get_currency_format(CURRENCY_SYMBOL, round(premium_sales / n_premium, 2))}")
    print(
        f"Vuelo Pasajeros más alto: \n {sorted_reports_seat[-1].code_route} -"
        f"{sorted_reports_seat[-1].n_seat_sales}")
    print(
        f"Vuelo Pasajeros más bajo: \n {sorted_reports_seat[0].code_route} -"
        f"{sorted_reports_seat[0].n_seat_sales}")
    print(
        f"Tres primeros vuelos con mayores ingresos: \n "
        f"{sorted_reports_sale[-1].code_route} \n "
        f"{sorted_reports_sale[-2].code_route} \n {sorted_reports_sale[-3].code_route}")
    
    print(
        f"Avion Pasajeros más bajo: {sorted_reports_seat[-1].name_airplane}")
    print(
        f"Avion Pasajeros más alto: {sorted_reports_seat[0].name_airplane}")
    print("\n")
    print("-"*30)
    print("\n")


if __name__ == "__main__":
    main()
