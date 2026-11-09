

#1-DEFINICIONES------------------------------------------------
#a: int = 17;
#b: int = 5;

def ejecutar_operaciones(a: int, b: int)-> None:
    print("Ejecutando operaciones aritméticas...")
    print("Suma: ",a+b)
    print("Resta:", a - b)            # 12
    print("Multiplicación:", a * b)   # 85
    print("División:", a / b)         # 3.4
    print("División entera:", a // b) # 3
    print("Módulo:", a % b)           # 2
    print("Potencia:", a ** 2)        # 289

def ejecutar_operaciones_con_precedencia()-> None:
    print("Ejecutando operaciones aritméticas con precedencia...")
    print(2 + 3 * 4)            #= 2 + (3* 4) 
    print((2 + 3) * 4)   # 20
    print(-2 ** 2)       # -4  (la potencia va antes que el signo)

def ejecutar_operaciones_asignacion()-> None:
    print("Ejecutando operaciones aritméticas con asignación...")
    x = 10
    x += 5    # x = x + 5   -> 15
    x -= 3    # x = x - 3   -> 12
    x *= 2    # x = x * 2   -> 24
    x //= 5   # x = x // 5  -> 4
    x **= 3   # x = x ** 3  -> 64
    print(x)

