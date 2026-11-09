#BUENAS PRACTICAS DE SCOPE
from typing import Final

# 1--------------------------------------------------------------------------
total: int = 0

# ❌ Modifica una global
def sumar_global(x: int) -> None:
    global total
    total += x

# ✅ Entrada explícita, salida explícita
def sumar(total: int, x: int) -> int:
    return total + x


# 2--------------------------------------------------------------------------
#SOLO USAR GLOBALES CUANDO SON CONSTANTES

IVA: Final[float] = 0.19
URL_API: Final[str] = "https://api.ejemplo.com"

def precio_final(precio: float) -> float:
    return precio * (1 + IVA)


# 3--------------------------------------------------------------------------
#PARA ESTADOS USAR CLASES
class Contador:
    def __init__(self) -> None:
        self.cuenta: int = 0

    def siguiente(self) -> int:
        self.cuenta += 1
        return self.cuenta

    def reiniciar(self) -> None:
        self.cuenta = 0