from fastapi import FastAPI
from models.tipo_mov_API import TipoMovAPI
from models.ingreso import Ingreso
from typing import Dict
from db import user_db
from db.user_db import database_users #importar db de users
from db.user_db import UserInDB
from models.user_models import UserIn, UserOut
from db.user_db import update_user, get_user

api = FastAPI()

@api.get("/")
async def home():
        return{"message": "Bienvenido a su gestor de gastos ByrsApp"}

@api.get("/tipos_movimiento/")
def getAllMovements():
   
    listMov = [
        TipoMovAPI(**{"id":1, "descr":"Comida"}),
        TipoMovAPI(**{"id":2, "descr":"Arriendo"}),
        TipoMovAPI(**{"id":3, "descr":"Transporte"})
    ]
    return{
        "typesMov": listMov
    }

@api.post("/ingreso")
def saveIncome(ingreso: Ingreso):
    print(ingreso)
    
@api.put("/users/") # actualizar post
def modify_user(user : UserInDB):
    database_users[user.username] = user
    return user

