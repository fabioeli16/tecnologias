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

Este ejercicio se realizo con el proposito de entender la importacion.

En especifico la importacion de codigo entre paquetes.

Los modulos estan en diferentes paquetes.

Se aprendio sobre alias

Se aprendio sobre importacion relativa

- Se resolvieron dudas:
    Uso de archivo __init__.py




<!------------------------------------------------------------------------------------------------------------------------------------------------------->
## Ejecucion

Comando para entrar a la ruta del script (relativo al repositorio):
cd PYTHON\importacion\2-importacion-entre-paquetes

Comando de windows y linux para ejecutar el script main:
python main.py

<!-- ............................... -->
- Ejecutar modulo dentro de paquete
cd PYTHON\importacion\2-importacion-entre-paquetes
python -m paquete_dos.modulo_importador

python -m paquete_uno.modulo_uno


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

-Las importaciones son objetos

-   Ejecutar siempre desde la raiz del proyecto
    .La importacion depende a la raiz del archivo que se ejecuta
    eje:
        cd PYTHON\importacion\2-importacion-entre-paquetes
        python main.py

- Usar importacion absoluta a la raiz del proyecto, si los paquetes y modulos son propios, eje:
    .Estructura:
        mi_proyecto/
        │
        ├── main.py
        │
        ├── servicios/
        │   ├── __init__.py
        │   └── usuarios.py
        │
        └── utilidades/
            ├── __init__.py
            └── fechas.py
    .importacion:
        Desde el archivo main.py, agregar la linea:
        import utilidades.fechas

- En proyectos medianos y grandes suele preferirse import porque hace el código más claro y evita conflictos de nombres.

    .EJEMPLO:
    import matematicas
    import estadisticas

    matematicas.media(datos)
    estadisticas.media(datos)

- No usar * Porque no sabes qué nombres fueron importados
    .EJEMPLO:
    from matematicas import *
    from estadisticas import *

    ¿De cuál módulo viene media?
        media(datos)