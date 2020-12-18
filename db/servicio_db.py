from datetime import datetime
from typing import List
from pydantic import BaseModel
from models.tipo_documento import tipo_documento
from models.documento import documento
from models.persona import persona
import uuid

#class servicio_db(BaseModel):

def save_tipo_documento(tipo_documento: tipo_documento):
    auto_tipo_documento["id"] = auto_tipo_documento["id"] + 1
    tipo_documento.id = auto_tipo_documento["id"]
    tipo_documento_db.append(tipo_documento)
    return tipo_documento

def save_documento(documento: documento):
    # Si el documento es del tipo No aplica, crea un guid para codigo
    auto_documento["id"] = auto_documento["id"] + 1
    documento.id = auto_documento["id"]
    if documento.tipo_documento.id == 0:
        documento.codigo = str(uuid.uuid4())
    documento_db.append(documento)
    return documento

def save_persona(persona: persona):
    auto_persona["id"] = auto_persona["id"] + 1
    persona.id = auto_persona["id"]
    #persona.documento = documento(tipo_documento = tipo_documento(id = 0),id = 0,codigo = "",fecha_vigencia = datetime.now())
        #persona.documento = documento(tipo_documento = 0)
    if persona.documento.tipo_documento.id == 0:
        persona.documento = save_documento(persona.documento)
    print(persona)
    persona_db.append(persona)
    print(persona_db)  
    return persona 

def update_persona(id: int, persona: persona):
    #if any(x.id == persona.id for x in persona_db):
    print(id)
    print(persona)
    persona_db[id] = persona
    
    return persona

def get_persona_id(id: int):
    if auto_persona["id"]>=id:
        return persona_db[id]
    else:
        return None

        



def initialize():
    # creo 3 tipos de documento
    noaplica = tipo_documento(id = 0,nombre = "No aplica",abreviatura = "N/A",vence = False)
    tipo_documento_db.append(noaplica)
    cedula = tipo_documento(id = 1,nombre = "Cédula de ciudadania",abreviatura = "C.C.",vence = False)
    tipo_documento_db.append(cedula)
    ce = tipo_documento(id = 2,nombre = "Cédula de extranjería",abreviatura = "C.E.",vence = False)
    tipo_documento_db.append(ce)
    # creo una persona, para evitar tanto codigo podria crear una funcion __init__ con valores por defecto
    mark = persona(id = 0,nombres = "Mark",apellidos = "Zuckerberg",fecha_nacimiento = datetime(1984,5,14),nacionalidad = "Estadounidense",
    documento = documento(id=0,tipo_documento = tipo_documento(),codigo = "",fecha_vigencia = datetime.max))
    persona_db.append(mark)




tipo_documento_db = []
auto_tipo_documento = {"id":2}

documento_db = []
auto_documento = {"id":0}

persona_db = []
auto_persona = {"id":0}

