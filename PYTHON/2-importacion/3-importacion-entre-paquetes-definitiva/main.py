#1-Importacion: 
# absoluta a la raiz del proyecto 
# Usando solo import para ayudar a la legibilidad
import paquete_uno.modulo_funciones as objeto_paquete_uno_modulo_funciones
import paquete_dos.modulo_funciones as objeto_paquete_dos_modulo_funciones



def main():

    print("*" * 75)
    resultado_suma_paquete_uno: int = objeto_paquete_uno_modulo_funciones.sumador_enteros(25,7)
    print(f"Resultado de la suma del objeto_paquete_uno_modulo_funciones: {resultado_suma_paquete_uno}")

    print("*" * 75)
    objeto_paquete_dos_modulo_funciones.sumador_enteros(2,5)
    objeto_paquete_dos_modulo_funciones.multiplicador_entero(2,5)

    print(f"Resultado de la suma del objeto_paquete_dos_modulo_funciones: {objeto_paquete_dos_modulo_funciones.resultado_suma}")
    print(f"Resultado de la multiplicacion del objeto_paquete_dos_modulo_funciones: {objeto_paquete_dos_modulo_funciones.resultado_multiplicacion}")


















if __name__ == "__main__":
    main()

