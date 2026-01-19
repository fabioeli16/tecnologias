#DEFINICION DE CLASE-ATRIBUTOS-METODOS
#ATRIBUTOS ESTATICOS
#ENCAPSULAMIENTO

#----------------------------------------------------------------------------------------------
#CLASE
from typing import ClassVar

class CuentaBancaria:
    #ATRIBUTO ESTATICO
    contadorInstancias: int = 0
    #ATRIBUTO ESTATICO USANDO CLASSVAR
    descripcionClase: ClassVar[str] = "Clase para crear cuentas bancarias"


    def __init__(self, titular: str, saldo_inicial: float) -> None:
        self.titular                :str    = titular  # público
        self.__saldo                :float  = saldo_inicial  # privado
        self.__contadorEncapsulado  :int    = 0
        self.contadorNormal         :int    =0
        CuentaBancaria.contadorInstancias+=1
    
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            return True
        return False
    
    def consultar_saldo(self):
        return self.__saldo
    
    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            return True
        return False
    
    def set_contador(self):
        self.__contadorEncapsulado+= 1
        self.contadorNormal+=1

    def get_contador(self):
        return {
            "contador encapsulado": self.__contadorEncapsulado,
            "contador Normal": self.contadorNormal
        }
    
    @classmethod
    def Set_contador_estatico(cls) -> None:
        cls.contadorInstancias += 1

    def get_contador_estatico(self) -> int:
        return CuentaBancaria.contadorInstancias
    
    def get_descripcion_estatica(self) -> str:
        return CuentaBancaria.descripcionClase






#----------------------------------------------------------------------------------------------
#MAIN
def main():
    # Uso OBJETO 1
    cuenta = CuentaBancaria("Eli", 1000)
    print(cuenta.titular)  # ✓ Funciona
    print(cuenta.consultar_saldo())  # ✓ 1000
    # print(cuenta.__saldo)  # ✗ Error: AttributeError
    cuenta.set_contador()
    cuenta.set_contador()
    print(cuenta.get_contador())  


    cuenta2 = CuentaBancaria("Fabio Eli", 2500)
    cuenta2.set_contador()
    cuenta2.set_contador()
    print(cuenta2.get_contador())  

    cuenta3 = CuentaBancaria("Eli Gomez", 1000)
    cuenta3.Set_contador_estatico()

    print(f"Contador de instancias: {cuenta2.get_contador_estatico()}")
    print(f"Contador de instancias: {cuenta.get_contador_estatico()}")
    print(f"Descripcion de la clase: {cuenta.get_descripcion_estatica()}")



if __name__ == "__main__":
    main()