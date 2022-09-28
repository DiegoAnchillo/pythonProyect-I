from __future__ import annotations

from typing import List, Dict
from model.Route import Route

def create_list_route() -> List[Route]:
    
    data_routes: List[Dict[str, str | float | int]]= [
        {
            "code": "LIM-AYA",
            "name": "LIMA-AYACUCHO",
            "base_price": 55.19,
            "economic": 8.00,
            "premium": 16.00,
            "min_sales_economic": 120,
            "max_sales_economic": 130,
            "min_sales_premium": 10,
            "max_sales_premium": 20
        },
        {
            "code": "LIM-CUS",
            "name": "LIMA-CUSCO",
            "base_price": 136.51,
            "economic": 8.00,
            "premium": 16.00,
            "min_sales_economic": 130,
            "max_sales_economic": 144,
            "min_sales_premium": 15,
            "max_sales_premium": 24
        },
        {
            "code": "LIM-ARE",
            "name": "LIMA-AREQUIPA",
            "base_price": 90.59,
            "economic": 8.00,
            "premium": 16.00,
            "min_sales_economic": 115,
            "max_sales_economic": 138,
            "min_sales_premium": 16,
            "max_sales_premium": 22
        },
        {
            "code": "LIM-TAR",
            "name": "LIMA-TARAPOTO",
            "base_price": 71.89,
            "economic": 8.00,
            "premium": 16.00,
            "min_sales_economic": 100,
            "max_sales_economic": 120,
            "min_sales_premium": 12,
            "max_sales_premium": 18
        },
        {
            "code": "AYA-LIM",
            "name": "AYACUCHO-LIMA",
            "base_price": 40.42,
            "economic": 7.00,
            "premium": 16.00,
            "min_sales_economic": 100,
            "max_sales_economic": 115,
            "min_sales_premium": 10,
            "max_sales_premium": 15
        },
        {
            "code": "CUS-LIM",
            "name": "CUSCO-LIMA",
            "base_price": 124.32,
            "economic": 7.00,
            "premium": 16.00,
            "min_sales_economic": 105,
            "max_sales_economic": 120,
            "min_sales_premium": 14,
            "max_sales_premium": 20
        },
        {
            "code": "ARE-LIM",
            "name": "AREQUIPA-LIMA",
            "base_price": 86.59,
            "economic": 7.00,
            "premium": 16.00,
            "min_sales_economic": 100,
            "max_sales_economic": 110,
            "min_sales_premium": 13,
            "max_sales_premium": 18
        },
        {
            "code": "TAR-LIM",
            "name": "TARAPOTO-LIMA",
            "base_price": 68.42,
            "economic": 7.00,
            "premium": 16.00,
            "min_sales_economic": 90,
            "max_sales_economic": 105,
            "min_sales_premium": 10,
            "max_sales_premium": 15
        }
    ]
    data_plane: List[Dict[str | int]]=[
        {
            "name": "A001",
            "n_seat" : 168
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