from datetime import datetime
from pydantic import BaseModel


class tipo_documento(BaseModel):
    id: int = 0
    nombre: str = ""
    vence: bool = False
'''
    def __init__(self,id,nombre,vence):
        self.id = 0
        self.nombre = nombre
        self.vence = vence
        '''
'''    
class tipo_documentoIn():
    id: int = 0
    nombre: str = ""
    vence: bool = False


    def create_from(self,inobj: tipo_documentoId):
        self.id = inobj.id
        self.nombre = inobj.nombre
        self.vence = inobj.vence 

    
    '''