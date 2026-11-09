
#1-DEFINICION VARIABLE-------------------------
x: str = "Global"

#2-DEFINICION FUNCION---------------------------
def funcion_externa():
    x: str = "Enclosing"

    def funcion_interna():
        x: str = "Local"
        print(x)    #Local

    funcion_interna()
    print(x)    #Enclosing

#3-SALIDA--------------------------------------
print("*" * 75)
print("modulo scope_leer_1.py")
funcion_externa()
print(x)