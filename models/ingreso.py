from pydantic import BaseModel

class Ingreso(BaseModel):
    idTipoMovimiento: int
    value: str