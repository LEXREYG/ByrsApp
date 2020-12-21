from pydantic import BaseModel


class tipo_documento(BaseModel):
    id: int = 0
    nombre: str = ""
    abreviatura: str = ""
    vence: bool = False
