from datetime import datetime
from pydantic import BaseModel
from models.tipo_documento import tipo_documento

class documento(BaseModel):
    id: int
    tipo_documento: tipo_documento
    codigo: str
    fecha_vigencia: datetime
'''
    def __init__(self,id,tipo_documento,codigo,fecha_vigencia):
        self.id = id
        self.tipo_documento = tipo_documento
        self.codigo = codigo
        self.fecha_vigencia = fecha_vigencia
'''
