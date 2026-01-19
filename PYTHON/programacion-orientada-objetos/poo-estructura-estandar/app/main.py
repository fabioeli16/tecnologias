# ============================================
# main.py
# ============================================

from app.services.banco_service import BancoService


def main():
    # Crear el banco
    banco = BancoService("Banco Nacional")
    
    # Crear cuentas
    cuenta1 = banco.crear_cuenta("Juan Pérez", 1000)
    cuenta2 = banco.crear_cuenta("María García", 500)
    cuenta3 = banco.crear_cuenta("Pedro López", 2000)
    
    print(f"=== {banco.nombre_banco} ===\n")
    
    # Mostrar cuentas
    print("Cuentas creadas:")
    for cuenta in banco.listar_cuentas():
        print(f"  {cuenta}")
    
    print(f"\nTotal depositado en el banco: ${banco.total_depositado():,.2f}")
    
    # Realizar operaciones
    print("\n=== Operaciones ===")
    cuenta1.depositar(500)
    print(f"Depósito de $500 en {cuenta1.numero_cuenta}")
    
    cuenta1.retirar(200)
    print(f"Retiro de $200 de {cuenta1.numero_cuenta}")
    
    cuenta1.transferir(cuenta2, 300)
    print(f"Transferencia de $300 de {cuenta1.numero_cuenta} a {cuenta2.numero_cuenta}")
    
    # Mostrar estado final
    print("\n=== Estado Final ===")
    for cuenta in banco.listar_cuentas():
        print(f"  {cuenta}")
    
    # Mostrar historial de una cuenta
    print(f"\nHistorial de {cuenta1.numero_cuenta}:")
    for transaccion in cuenta1.obtener_historial():
        print(f"  {transaccion['fecha'].strftime('%Y-%m-%d %H:%M:%S')} - "
              f"{transaccion['tipo']}: ${transaccion['monto']:,.2f} - "
              f"Saldo: ${transaccion['saldo_resultante']:,.2f}")


if __name__ == "__main__":
    main()