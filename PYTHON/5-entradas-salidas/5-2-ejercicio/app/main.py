import funciones.salida_datos as salida
import logica.generador_recibo as recibo

def main():
    encabezado: list[str] = ["Producto", "Precio", "Cantidad"]

    print(recibo.compras)

    for compra in recibo.compras:
        print(f"Producto: {compra['nombre']}, Precio: {compra['precio']}, Cantidad: {compra['cantidad']}")

    print("-"*40)
    print(*encabezado, sep="\t")
    salida.mostrar_lista_de_diccionarios(recibo.compras)





if __name__ == "__main__":
    main()
