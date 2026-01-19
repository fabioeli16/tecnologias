# ============================================
# src/models/cuenta_bancaria.py
# ============================================

class CuentaBancaria:
    """Modelo que representa una cuenta bancaria."""
    
    def __init__(self, numero_cuenta, titular, saldo_inicial=0):
        self.__numero_cuenta = numero_cuenta
        self.__titular = titular
        self.__saldo = saldo_inicial
        self.__transacciones = []
    
    @property
    def numero_cuenta(self):
        return self.__numero_cuenta
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def saldo(self):
        return self.__saldo
    
    def depositar(self, cantidad):
        """Deposita dinero en la cuenta."""
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        
        self.__saldo += cantidad
        self.__registrar_transaccion("Depósito", cantidad)
        return True
    
    def retirar(self, cantidad):
        """Retira dinero de la cuenta."""
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        
        if cantidad > self.__saldo:
            raise ValueError("Saldo insuficiente")
        
        self.__saldo -= cantidad
        self.__registrar_transaccion("Retiro", cantidad)
        return True
    
    def transferir(self, cuenta_destino, cantidad):
        """Transfiere dinero a otra cuenta."""
        self.retirar(cantidad)
        cuenta_destino.depositar(cantidad)
        self.__registrar_transaccion(f"Transferencia a {cuenta_destino.numero_cuenta}", cantidad)
    
    def obtener_historial(self):
        """Retorna el historial de transacciones."""
        return self.__transacciones.copy()
    
    def __registrar_transaccion(self, tipo, monto):
        """Método privado para registrar transacciones."""
        from datetime import datetime
        self.__transacciones.append({
            'fecha': datetime.now(),
            'tipo': tipo,
            'monto': monto,
            'saldo_resultante': self.__saldo
        })
    
    def __str__(self):
        return f"Cuenta {self.__numero_cuenta} - Titular: {self.__titular} - Saldo: ${self.__saldo:,.2f}"
