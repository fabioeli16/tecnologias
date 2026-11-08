
#1-IMPORTACION DEL MODULO COMO OBJETO
#import modulo_funciones

#2-IMPORTACION DEL CONTENIDO DEL MODULO
#from modulo_funciones import *

#3-IMPORTACION DE UN CONTENIDO DEL MODULO
#from modulo_funciones import sumador_enteros

#4-ESTA ES UNA IMPORTACION EN CADENA: EL MODULO IMPORTADO, IMPORTA OTRO MODULO
from modulo_importador import *


def main():
    #EJECUCION DE LA IMPORTACION 1
    #print(modulo_funciones.sumador_enteros(5, 3))
    
    #EJECUCION DE LA IMPORTACION 2, 3, 4   
    print(sumador_enteros(5, 3))
    print(f"Resultado resta: {restador_enteros(5)}")


if __name__ == "__main__":
    main()