from pydantic import BaseModel
from datetime import datetime

class PersonaIn(BaseModel):
    id: int

class PersonaOut(BaseModel):
    id: int
    nombres: str
    apellidos: str
    fecha_nacimiento: datetime
    nacionalidad: str
    documento: str
    saldo: int
