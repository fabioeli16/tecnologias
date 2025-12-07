from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()

# Ruta absoluta de templates no necesaria, FastAPI la detecta desde donde ejecutas uvicorn
templates = Jinja2Templates(directory="templates")


# END POINT´S----------------------------------------------------------
# ---- API SIMPLE ----
@app.get("/api/saludo")
def api_saludo():
    return {"mensaje": "Hola desde la API"}

# ---- RETORNAR HTML ----
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "titulo": "Mi primera página",
            "mensaje": "Bienvenido a FastAPI + Jinja2"        
        }
    )

# ---- RETORNAR HTML + LOGICA----
@app.get("/usuario", response_class=HTMLResponse)
def usuario(request: Request):

    # Array de usuarios (puede venir de BD luego)
    lista_usuarios = [
        {"id": 1, "nombre": "Juan", "edad": 28},
        {"id": 2, "nombre": "María", "edad": 34},
        {"id": 3, "nombre": "Carlos", "edad": 22},
    ]

    return templates.TemplateResponse(
        "usuario.html",
        {
            "request": request,
            "usuarios": lista_usuarios
        }
    )


#HANDLERS
@app.exception_handler(StarletteHTTPException)
async def custom_404_handler(request: Request, exc: StarletteHTTPException):
    if exc.status_code == 404:
        return templates.TemplateResponse(
            "404.html",
            {"request": request, "ruta": request.url.path},
            status_code=404
        )
    raise exc  # otros códigos de error