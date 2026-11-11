import salidas as salidas
import entrada as entrada




def main():
    salidas.mostrar_mensaje()
    salidas.formatear()
    salidas.fecha_hora_actual()
    numero: int = entrada.entrada_numero("Ingresa un número entero: ")
    print(f"El número ingresado es: {numero}")



if __name__ == "__main__":
    main()
