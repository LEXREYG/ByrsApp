from datetime import datetime
from typing import  Dict
from pydantic import BaseModel

class PersonaInDB(BaseModel):
    id: int = 0
    nombres: str
    apellidos: str
    fecha_nacimiento: datetime
    nacionalidad: str
    documento: str
    saldo: int

database_personas = Dict[str, PersonaInDB]

database_personas = {
    "0": PersonaInDB(**{
        "id": 0,
        "nombres": "Mark",
        "apellidos": "Zuckerberg", 
        "fecha_nacimiento": datetime(1984,5,14),
        "nacionalidad": "Estadounidense",
        "documento": "CC",
        "saldo": 100000
    }),
    "1": PersonaInDB(**{
        "id": 1,
        "nombres": "Bill",
        "apellidos": "Gates",
        "fecha_nacimiento": datetime(1962,11,30),
        "nacionalidad": "Canadiense",
        "documento": "TI",
        "saldo": 200000
    }),

    "2": PersonaInDB(**{
        "id": 2,
        "nombres": "Elthon",
        "apellidos": "Musk",
        "fecha_nacimiento": datetime(1969,1,25),
        "nacionalidad": "Australiano",
        "documento": "RC",
        "saldo": 300000
    }),
}

def get_persona(id: str):

    if id in database_personas.keys():
        return database_personas[id]
    else:
        return None

def update_persona(persona_in_db: PersonaInDB):
    database_personas[persona_in_db.id] = persona_in_db
    return persona_in_db
