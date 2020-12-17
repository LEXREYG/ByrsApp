from fastapi import FastAPI
from models.tipo_documento import tipo_documento
from models.documento import documento
from models.persona import persona
from db import servicio_db
'''
from models.tipo_mov_API import TipoMovAPI
from models.ingreso import Ingreso
from typing import Dict
from db import user_db
from db.user_db import database_users #importar db de users
from db.user_db import UserInDB
from models.user_models import UserIn, UserOut
from db.user_db import update_user, get_user
'''
api = FastAPI()
service = servicio_db
service.initialize()

@api.get("/")
async def home():
    return{"message": "Bienvenido a su gestor de gastos ByrsApp"}

@api.get("/tipo_documento/")
def get_all_tipo_documento():
    return service.tipo_documento_db

@api.post("/tipo_documento/")
def post_tipo_documento(item: tipo_documento):
    return service.save_tipo_documento(item)

@api.get("/persona")
def get_all_persona():
    return service.persona_db

@api.post("/persona/")
def post_persona(item: persona):
    print(item)
    return service.save_persona(item)
    print("Algo 8")  

@api.put("/persona/{item_id}") #,response_model = persona
def put_persona(item_id: str,item: persona):
    return service.update_persona(int(item_id), item)

'''
@api.post("/ingreso")
def saveIncome(ingreso: Ingreso):
    print(ingreso)
    
@api.put("/users/") # actualizar post
def modify_user(user : UserInDB):
    database_users[user.username] = user
    return user
'''
