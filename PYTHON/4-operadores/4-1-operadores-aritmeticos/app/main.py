from app.config.settings import DEBUG, get_settings
import app.operaciones as operaciones
import app.ejercicio as ejercicio

a: int = 17;
b: int = 5;



def main():
    operaciones.ejecutar_operaciones(a, b)
    operaciones.ejecutar_operaciones_con_precedencia()
    operaciones.ejecutar_operaciones_asignacion()
    resultado: str = ejercicio.convertir_segundos_a_tiempo(3725)
    print(f"Tiempo convertido: {resultado}")

if __name__ == "__main__":
    main()
