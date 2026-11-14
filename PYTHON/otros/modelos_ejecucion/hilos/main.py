import time
from concurrent.futures import ThreadPoolExecutor

def tarea_con_retraso(operador:int)->int:
    triplicar: int = operador * 3
    retraso: int = 3
    time.sleep(retraso)          # simula esperar una respuesta de red

    return triplicar


def main():


    #Ejecucion secuencial----------------------------------------------------------
    print("Inicio ejecucion secuencial","*"*10)
    operador: int = 5
    resultado: int
    resultado_tareas: list[int]
    inicio = time.perf_counter()

    resultado = tarea_con_retraso(operador)
    print(f"Resultado: {resultado}")

    resultado_tareas = [
        tarea_con_retraso(i)
        for i in range(1,4)
    ]
    for res in resultado_tareas:
        print("Resultado: ",res)

    print("Final:", resultado_tareas, f"{time.perf_counter() - inicio:.1f}s")

    #Ejecucion con hilos----------------------------------------------------------
    print("Inicio ejecucion con hilos","*"*10)
    operadores: list[int] = [2,3,5]
    resultado_tareas_hilos: list[int]
    inicio = time.perf_counter()
    with ThreadPoolExecutor() as ejecutador:
        resultado_tareas_hilos = list(ejecutador.map(tarea_con_retraso, operadores))
    print("Hilos:     ", resultado_tareas_hilos, f"{time.perf_counter() - inicio:.1f}s")



    

if __name__ == "__main__":
    main()
