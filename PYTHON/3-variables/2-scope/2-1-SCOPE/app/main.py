import app.config.settings as configuraciones
import app.scope_leer_1 as scope1
import app.scope_asignar_2 as scope2
import app.sin_scope_3 as scope3


def main():
    print("*" * 75)
    print("INICIA MAIN")
    print(configuraciones.DEBUG)
    print(configuraciones.get_settings())



if __name__ == "__main__":
    main()
