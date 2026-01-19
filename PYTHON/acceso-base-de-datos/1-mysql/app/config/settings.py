import os
from dotenv import load_dotenv


#VARIABLES------------------------------------------------------------------
# VARIABLES DE ENTORNO
load_dotenv()                       # Carga las variables del archivo .env
APP = os.getenv("APP_ENV")
PROJECT = os.getenv("PROJECT_NAME")
HOSTNAME = os.getenv("HOST_NAME")
ROOT = os.getenv("PROJECT_ROOT_ENV")    #VARIABLE DEFINIDA POR LA POWER SHELL
#VARIABLES DEL MODULO
DEBUG = True

#FUNCIONES-------------------------------------------------------------------
def get_settings():
    return {
        "debug": DEBUG,
        "project_root": ROOT,
        "app_env": APP,
        "project_name":PROJECT
    }

def get_host()->str:
    return HOSTNAME