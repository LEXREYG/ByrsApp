from datetime import datetime
from pydantic import BaseModel
from models.tipo_documento import tipo_documento

class documento(BaseModel):
    id: int
    tipo_documento: tipo_documento
    codigo: str
    fecha_vigencia: datetime
