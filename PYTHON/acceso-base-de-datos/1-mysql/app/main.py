from app.config.settings import *
import mysql.connector
from mysql.connector import Error


def conectar_mysql():
    try:
        conexion = mysql.connector.connect(
            host=get_host(),
            port=3390,
            user="root",
            password="S3m4f0r02020*",
            database="semaforo_web"
        )

        if conexion.is_connected():
            print("✅ Conexión exitosa a MySQL")
            return conexion

    except Error as e:
        print(f"❌ Error al conectar a MySQL: {e}")
        return None

def obtener_usuarios(conn)->None:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios LIMIT 10")

    for fila in cursor.fetchall():
        print(fila)




if __name__ == "__main__":
    conn = conectar_mysql()

    if conn:
        obtener_usuarios(conn)
        conn.close()
        print("🔌 Conexión cerrada")
