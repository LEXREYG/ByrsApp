from fastapi import FastAPI
from db.personas_db import update_persona, get_persona, PersonaInDB
from db.transacciones_db import update_transaccion, get_transaccion, get_transacciones, TransaccionInDB
from fastapi import FastAPI, HTTPException
from models.tipo_documento import tipo_documento
from models.documento import documento
from models.persona import PersonaIn, PersonaOut
from models.transaccion import TransaccionIn, TransaccionOut
from fastapi.middleware.cors import CORSMiddleware

api = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@api.get("/")
async def home():
    return{"message": "Bienvenido a su gestor de gastos ByrsApp"}

@api.get("/persona/{id_persona}")

async def get_tercero(id_persona: str):
    persona_out = get_persona(id_persona)
    if persona_out == None:
        raise HTTPException(status_code=404, detail="El tercero no existe")

    return  persona_out


@api.post("/transaccion/")
async def crear_transaccion(transaccion_in: TransaccionInDB):
    transaccion = update_transaccion(transaccion_in)
    return transaccion_in

@api.get("/transaccion/consulta/")

async def cargar_trancciones():
    transacciones = get_transacciones()
    if transacciones == None:
        raise HTTPException(status_code=404, detail="No existe movimiento")

    return  transacciones
