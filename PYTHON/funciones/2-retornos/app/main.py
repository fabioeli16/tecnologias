import app.paquete_funciones.funciones as objeto_funciones

def main():

    #---------------------------------------------------------------------------------
    nombre: str;
    edad: int;
    mis_datos: tuple;


    nombre, edad= objeto_funciones.obtener_datos();
    print("+"*50)
    print(f"Los valores retornados fueron: {nombre, edad}");
    print(f"Tipo de la variable: {type(nombre)}");

    print("+"*50)
    mis_datos = objeto_funciones.obtener_datos();
    print("Los valores capturados como tupla son:")
    print(mis_datos[0])
    print(mis_datos[1])
    print(f"Tipo de la variable: {type(mis_datos)}");







    """
    #---------------------------------------------------------------------------------
    print("*" * 72)
    #Argumento nombrado - debe llamarse igual al parametro en la funcion
    objeto_funciones.saludar(nombre="Eli")
    #Sin argumento
    objeto_funciones.saludar()

    #---------------------------------------------------------------------------------
    #Parametros variables
    mis_numeros = (10, 20, 30, 40, 50)

    #Se envia la tupla desempaquetada
    sumatoria = objeto_funciones.sumador_varios_numeros(*mis_numeros)
    if sumatoria is None:
        print("La variable es None")
    else:
        print(f"Resultado de la sumatoria: {sumatoria}")
    sumatoria_dos = objeto_funciones.sumador_varios_numeros(1,2,3,4,5)
    print(f"Resultado de la sumatoria dos es: {sumatoria_dos}")
    """

if __name__ == "__main__":
    main()
