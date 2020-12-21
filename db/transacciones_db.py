from datetime import datetime
from typing import  Dict
from pydantic import BaseModel

class TransaccionInDB(BaseModel):
    id: int = 0
    valor: str
    tipo: str
    detalle: str
    fecha: datetime

database_transacciones = Dict[str, TransaccionInDB]

database_transacciones = {
    0: TransaccionInDB(**{
        "id": 0,
        "valor": 2000,
        "tipo": "Ingreso",
        "fecha": datetime(2020,12,21),
        "detalle": "Me encontre un billete"
    }),
    1: TransaccionInDB(**{
        "id": 1,
        "valor": 2500,
        "tipo": "Gasto",
        "fecha": datetime(2020,12,22),
        "detalle": "Pago desayuno"
    }),

    2: TransaccionInDB(**{
        "id": 2,
        "valor": 6000,
        "tipo": "Gasto",
        "fecha": datetime(2020,12,23),
        "detalle": "Transporte oficina"
    }),
}

def get_transacciones():
    if database_transacciones:
        return database_transacciones
    else:
        return None

def get_transaccion(id: str):
    if id in database_transacciones.keys():
        return database_transacciones[id]
    else:
        return None

def update_transaccion(transaccion_in_db: TransaccionInDB):
    database_transacciones[transaccion_in_db.id] = transaccion_in_db
    return transaccion_in_db
