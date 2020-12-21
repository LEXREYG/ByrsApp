from pydantic import BaseModel
from datetime import datetime

class TransaccionIn(BaseModel):
    id: int
    valor: int
    tipo: str
    detalle: str
    fecha: datetime

class TransaccionOut(BaseModel):
    id: int
    valor: int
    tipo: str
    detalle: str
    fecha: datetime
