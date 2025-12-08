import time
import concurrent.futures

def calculaConEspera(numero:int):
    print(f"calculando: {numero}")
    time.sleep(3)
    resultado = numero*2
    return resultado

def main():
    for i in range(10):
        res=calculaConEspera(i)
        print(f"Resultado: {res}")



if __name__== "__main__":
    main()

