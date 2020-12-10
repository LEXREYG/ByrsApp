from pydantic import BaseModel

class TipoMovAPI(BaseModel):
    id: int
    descr: str