# +IMPORTACION-1-ENTRE-PAQUETES

## Índice

- [Descripcion](#Descripcion)
- [Ejecucion](#Ejecucion)
- [Alias](#Alias)
- [Prompts](#Prompts)
- [Dudas](#Dudas)
- [Conclusiones](#Conclusiones)


<!------------------------------------------------------------------------------------------------------------------------------------------------------->
## Descripcion

Este ejercicio se realizo con el proposito de definir el estandar definitivo para la importacion de modulos entre paquetes.





<!------------------------------------------------------------------------------------------------------------------------------------------------------->
## Ejecucion

Comando para entrar a la ruta del script relativo al repositorio (compatible con Windows y linux):
cd PYTHON\importacion\3-importacion-entre-paquetes-definitiva

Comando para ejecutar el script main (compatible con Windows y linux):
python main.py


<!------------------------------------------------------------------------------------------------------------------------------------------------------->
## Prompts


Importacion de paquetes y modulos.

como importar un modulo "x" dentro de un paquete "paquete_x", desde un modulo "y" en un paquete "paquete_y". ambos paquetes estan en el mismo paquete.

cuando importo con "import" esto crea un objeto?

python. 
Como trabaja python los modulos importados? los convierte en diccionario, clases u objetos? porque y como los ejecuta al importarlos?

<!------------------------------------------------------------------------------------------------------------------------------------------------------->
## Dudas 

- Pasos que ejecuta PYTHON al importar
    1. Busca el archivo.
    2. Crea un objeto de tipo module.
    3. Ejecuta todo el código del archivo.
    4. Guarda el resultado en sys.modules.
    5. Expone las variables, funciones y clases mediante el diccionario interno __dict__.


- ¿Qué es un módulo cuando lo importas?
    Una instancia de una clase module o un objeto module

- Como funcionan internamente los modulos
    Cada módulo tiene un diccionario interno llamado __dict__   donde almacena 

- Que pasa si importo un modulo dos veces?
    El modulo importado se guarda en caché asi solo se ejecuta una vez

- ¿Importar el módulo completo consume más memoria que importar solo algunos elementos usando FROM?
    NO. consume los mismo.
    Es decir, estas dos instrucciones: import matematicas y from matematicas import sumar, normalmente hacen que Python cargue el mismo módulo en sys.modules.
    La diferencia principal es cómo accedes a los elementos

<!------------------------------------------------------------------------------------------------------------------------------------------------------->
## Conclusiones

- Las importaciones son objetos

- Ejecutar siempre desde la raiz del proyecto (VER ## Ejecucion)

- Usar importacion absoluta a la raiz del proyecto (ver main.py)

- En proyectos medianos y grandes usar import porque hace el código más claro y evita conflictos de nombres.

- No usar * Porque no sabes qué nombres fueron importados
