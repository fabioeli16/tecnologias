import datetime as datetime

def mostrar_mensaje()->None:
    nombre: str = "Eli"
    edad: int = 30
    print(f"Nombre: {nombre}, Edad: {edad}")
    print("\n")

def formatear()->None:
    total: float = 1234.5678
    millar: int = 1234567
    print(f"Total: {total:.2f}")      # Total: 1234.57    (2 decimales)
    print(f"Millar: {millar:,}")       # Millar: 1,234,567  (separador de miles)
    print(f"|{'Hola':>10}|")          # |      Hola|      (alineado a la derecha en 10 espacios)
    print(f"|{'Hola':<10}|")          # |Hola      |      (alineado a la izquierda)
    print(f"{0.856:.1%}")             # 85.6%             (porcentaje)

def fecha_hora_actual()->None:
    hoy = datetime.date.today()
    año = hoy.year
    mes = hoy.month
    dia = hoy.day

    print(año, mes, dia, sep="-")           # 2026-11-10
    print("Cargando", end="...\n")
    print("listo")                       
    print("\n")



