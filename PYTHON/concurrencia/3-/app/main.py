import sys
import app.config.settings as configuraciones


def main():
    print("...")
    #--------------------------------------------------------------------------------------------------
    #VALIDAR SI GIL ESTA ACTIVO
    gil_activo = getattr(sys, "_is_gil_enabled", lambda: True)()
    print(f"GIL activo: {gil_activo}")



if __name__ == "__main__":
    main()
