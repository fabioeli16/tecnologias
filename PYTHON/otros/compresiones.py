# SEMANTICA:        [RETORNO    ITERACION     CONDICIONAL/FILTRO]

import timeit



#1-COMPARACION DE SINTAXIS----------------------------------------------------------------------------------------------------
#1.1-DEFINICIONES PARA COMPARAR-------------------------
cuadrados = []
cuadrados2 = []

def sin_usar_comprension():
    for i in range(0,5):
        cuadrados.append(i**2)                  #NO ES NECESARIO USAR GLOBAL, YA QUE NO SE ESTA ASIGNANDO UN NUEVO VALOR A LA VARIABLE, SOLO SE ESTA MODIFICANDO SU CONTENIDO

def usando_comprension():
    global cuadrados2
    cuadrados2= [i**2 for i in range(0,5)]      #ES NECESARIO USAR GLOBAL, YA QUE SE ESTA ASIGNANDO UN NUEVO VALOR A LA VARIABLE, POR LO TANTO SE DEBE INDICAR QUE ES UNA VARIABLE GLOBAL


#1.2-SALIDAPARA COMPARAR --------------------------------
print("*" * 75)
sin_usar_comprension()
print(cuadrados)
for c in cuadrados:
    print(c)

usando_comprension()
print("*" * 75)
print(cuadrados2)
for c2 in cuadrados2:
    print(c2)


#2-COMPRESIONES SIMPLES PARA ENTENDER------------------------------------------------------------------------
print("*" * 75)
nombres = ["Juan", "Pedro", "Maria", "Ana", "Eli"]
nombres_cortos = [
    nombre                      #VALOR QUE SE VA A AGREGAR A LA NUEVA LISTA
    for nombre in nombres       #ITERACION SOBRE LA LISTA ORIGINAL
    if len(nombre) <= 3         #CONDICIONAL QUE FILTRA LOS ELEMENTOS DE LA LISTA ORIGINAL
]

for nombre in nombres_cortos:
    print(nombre)



#3-COMPARACION DE RENDIMIENTO------------------------------------------------------------------------
print("*" * 75)
def con_for():
    r = []
    for n in range(1000):
        r.append(n * 2)
    return r

def con_comprension():
    return [n * 2 for n in range(1000)]

print(timeit.timeit(con_for, number=10_000))
print(timeit.timeit(con_comprension, number=10_000))