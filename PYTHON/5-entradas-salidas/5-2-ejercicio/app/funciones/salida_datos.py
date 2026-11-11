

"""
    Esta función recibe una lista de diccionarios y muestra los datos de cada diccionario en un formato legible.
    Separa cada fila con una línea en blanco para mejorar la legibilidad.
    Separa los valores de cada diccionario con tabulaciones para que se vea como una tabla.
    Parámetros:
        lista (list[dict]): Una lista de diccionarios que contienen los datos a mostrar.
    Retorna:
        None"""
def mostrar_lista_de_diccionarios(lista: list[dict])->None:
    for fila in lista:
        for clave, valor in fila.items():
            print(f"{valor}",end="\t")  # tabulación entre columnas
        print()   # línea en blanco entre filas