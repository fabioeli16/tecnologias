from app.config.settings import DEBUG, get_settings
from fastapi import FastAPI

app = FastAPI(
    title="API Simple",
    description="API de ejemplo usando FastAPI",
    version="1.0.0"
)


"""
# DESACTIVAR DOCUMENTACION (PARA PRODUCCION)
app = FastAPI(
    docs_url=None,
    redoc_url=None,
    openapi_url=None
)
"""


@app.get("/")
def read_root():
    return {"mensaje": "Hola mundo desde FastAPI"}



@app.get(
    "/saludo/{nombre}",
    summary="Saludar usuario",
    description="Devuelve un saludo usando el nombre enviado"
)
def saludar(nombre: str):
    return {"saludo": f"Hola {nombre}, bienvenido a FastAPI"}



@app.get("/suma")
def sumar(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "resultado": a + b
    }



@app.get(
    "/items/{id}",
    responses={
        200: {"description": "Item encontrado"},
        404: {"description": "Item no encontrado"}
    }
)
def get_item(id: int):
    return {"id": id}