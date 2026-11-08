import sys
import math as mi_objeto_math
from types import ModuleType

#1-Importacion: absoluta a la raiz del proyecto - completa - SE EJECUTA UNBA SOLO VEZ AL IMPORTAR
import paquete_uno.modulo_uno as objeto_modulo
import paquete_uno.modulo_uno as objeto2_modulo

#2- Importacion por partes - 
#Observacion: las variables se vuelven objetos independiente pero las funciones si hacen referencia al mismo objeto importado en la importacion 1 (de arriba)
from paquete_uno.modulo_uno import numero as objeto_numero
from paquete_uno.modulo_uno import numero as objeto_numero2
from paquete_uno.modulo_uno import funcion_asignar_valor as objeto_funcion


def main():

    #VALIDA QUE TODO LO IMPORTADO ES UNA INSTANCIA/OBJETO--------------------------------------------
    print("*" * 50)
    mi_objeto_modulo = ModuleType("mi_modulo")
    print("clase del objeto mi_objeto_modulo: ",type(mi_objeto_modulo))
    print("confirmar instancia de objeto mi_objeto_modulo a la clase ModuleType: ",isinstance(mi_objeto_modulo, ModuleType))

    print("clase del objeto mi_objeto_math: ",type(mi_objeto_math))
    print("confirmar instancia de objeto mi_objeto_math a la clase ModuleType: ",isinstance(mi_objeto_math, ModuleType))

    print("clase del objeto objeto_modulo: ",type(objeto_modulo))
    print("confirmar instancia de objeto modulo_uno.objeto_modulo a la clase ModuleType: ",isinstance(objeto_modulo, ModuleType))


    #VALIDA LA INSTANCIA DE LO IMPORTADO------------------------------------------------------------
    print("*" * 50)
    print("clase del objeto modulo: ",type(objeto_modulo))
    print(id(objeto_modulo))

    #print(modulo.__dict__)
    print(objeto_modulo.numero)
    print(objeto2_modulo.funcion_asignar_valor(5))
    print(objeto_modulo.numero)
    print(objeto2_modulo.numero)


    print("ID del objeto objeto_modulo.numero: ",id(objeto_modulo.numero))
    print("ID del objeto objeto2_modulo.numero ",id(objeto2_modulo.numero))
    print("ID del objeto objeto_numero: ",id(objeto_numero))
    print("Valor del objeto numero: ",objeto_numero)
    print("ID del objeto numero 2: ",id(objeto_numero2))
    print("Valor del objeto numero 2: ",objeto_numero2)
    print("clase del objeto numero importado de modulo_uno: ",type(objeto_modulo))
    print("ID del objeto funcion: ",id(objeto_funcion))
    print("ID de la funcion en el objeto modulo:",id(objeto2_modulo.funcion_asignar_valor))

    print("clase del objeto objeto_funcion importado de modulo_uno: ",type(objeto_funcion))

    objeto_funcion(10)
    print(objeto_modulo.numero)
    print(objeto2_modulo.numero)






    #VALIDA LOS MODULOS IMPORTADOS-------------------------------------------------------------------
    print("*" * 50)
    """
    for nombre in sys.modules:
        print(nombre)
        """




















if __name__ == "__main__":
    main()

