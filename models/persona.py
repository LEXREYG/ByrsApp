from datetime import datetime
from pydantic import BaseModel
from models.documento import documento

class persona(BaseModel):
    id: int
    nombres: str
    apellidos: str
    fecha_nacimiento: datetime
    nacionalidad: str
    documento: documento
'''
    def __init__(self,id,nombres,apellidos,fecha_nacimiento,nacionalidad,documento):
        self.id = id
        self.nombres = nombres
        self.apellidos = apellidos
        self.fecha_nacimiento = fecha_nacimiento
        self.nacionalidad = nacionalidad
        self.documento = documento
'''
