# Calculadora de notas

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))

# Validación con comparaciones encadenadas
if not (0 <= nota1 <= 5 and 0 <= nota2 <= 5 and 0 <= nota3 <= 5):
    print("Error: todas las notas deben estar entre 0 y 5.")
else:
    promedio = (nota1 + nota2 + nota3) / 3
    print(f"Promedio: {promedio:.2f}")

    if promedio >= 3.0:
        print("Resultado: APROBÓ ✅")
    else:
        faltante = 3.0 - promedio
        print(f"Resultado: REPROBÓ ❌ (le faltan {faltante:.2f} puntos)")

    # Bonus 1: parte entera par o impar
    parte_entera = int(promedio // 1)
    if parte_entera % 2 == 0:
        print(f"La parte entera ({parte_entera}) es par")
    else:
        print(f"La parte entera ({parte_entera}) es impar")

    # Bonus 2: nota necesaria en un 4.º examen para que el promedio sea 3.0
    # (n1 + n2 + n3 + x) / 4 = 3.0  ->  x = 12 - (n1 + n2 + n3)
    necesaria = 3.0 * 4 - (nota1 + nota2 + nota3)
    if necesaria <= 0:
        print("Ya tiene asegurado el 3.0 aunque saque 0 en el 4.º examen.")
    elif necesaria > 5:
        print(f"Necesitaría {necesaria:.2f}: no es posible con una nota máxima de 5.")
    else:
        print(f"Necesita al menos {necesaria:.2f} en el 4.º examen.")