import sys

#1-Importacion: absoluta a la raiz del proyecto - por partes
#from paquete_uno.modulo_funciones import sumador_enteros, resultado_suma

#2-Importacion: absoluta a la raiz del proyecto - completa
import paquete_uno.modulo_funciones as funciones

#2-IMportacion relativa (da error)
#from ..paquete_uno.modulo_funciones import *


if __name__ == "__main__":
    
    #EJECUCION DE LA IMPORTACION 1  
    """
    print("Ejecutando directamente este archivo")
    mi_resultado: int = sumador_enteros(2,5)

    print("Resultado variable local: ",mi_resultado)
    print("Resultado variable importada: ",resultado_suma)
    """

    #EJECUCION DE LA IMPORTACION 2  
    print("Ejecutando directamente este archivo")
    mi_resultado = funciones.sumador_enteros(2,5)

    print("Resultado variable local:", mi_resultado)
    print("Resultado variable del módulo:", funciones.resultado_suma)

    #----------------------------------------------------------------------------------------
    #VER MODULOS
    for nombre in sys.modules:
        print(nombre)
    
