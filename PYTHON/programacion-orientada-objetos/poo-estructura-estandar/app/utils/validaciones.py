# ============================================
# src/utils/validaciones.py
# ============================================

def validar_monto(monto):
    """Valida que el monto sea válido."""
    if not isinstance(monto, (int, float)):
        raise TypeError("El monto debe ser un número")
    if monto <= 0:
        raise ValueError("El monto debe ser mayor a cero")
    return True


def validar_titular(nombre):
    """Valida que el nombre del titular sea válido."""
    if not isinstance(nombre, str):
        raise TypeError("El nombre debe ser una cadena de texto")
    if len(nombre.strip()) < 3:
        raise ValueError("El nombre debe tener al menos 3 caracteres")
    return True