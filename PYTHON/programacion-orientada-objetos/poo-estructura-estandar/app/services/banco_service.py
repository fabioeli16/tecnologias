# ============================================
# src/services/banco_service.py
# ============================================
from app.models.cuenta_bancaria import CuentaBancaria


class BancoService:
    """Servicio que gestiona múltiples cuentas bancarias."""
    
    def __init__(self, nombre_banco):
        self.__nombre_banco = nombre_banco
        self.__cuentas = {}
        self.__contador_cuentas = 1000
    
    def crear_cuenta(self, titular, saldo_inicial=0):
        """Crea una nueva cuenta bancaria."""
        
        numero_cuenta = f"CTA-{self.__contador_cuentas}"
        self.__contador_cuentas += 1
        
        nueva_cuenta = CuentaBancaria(numero_cuenta, titular, saldo_inicial)
        self.__cuentas[numero_cuenta] = nueva_cuenta
        
        return nueva_cuenta
    
    def buscar_cuenta(self, numero_cuenta):
        """Busca una cuenta por su número."""
        return self.__cuentas.get(numero_cuenta)
    
    def listar_cuentas(self):
        """Lista todas las cuentas del banco."""
        return list(self.__cuentas.values())
    
    def total_depositado(self):
        """Calcula el total de dinero en el banco."""
        return sum(cuenta.saldo for cuenta in self.__cuentas.values())
    
    @property
    def nombre_banco(self):
        return self.__nombre_banco
