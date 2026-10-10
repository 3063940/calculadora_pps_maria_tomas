"""
Aplicación de Calculadora de la tarea 1 de Puesta en Producción segura.
Bloque E, después de refactorizar y añadir algunos de los requisitos de 
esta tarea. 
"""
MAX_INTENTOS = 10
MAX_CANTIDAD = 10000
MAX_PRECIO = 1000000


def calcular_total(cantidad, precio):
    """Calcula el importe total multiplicando cantidad por precio."""
    return cantidad * precio


def pedir_cantidad():
    """Solicita y valida la cantidad de productos."""
    intentos = 0

    while intentos < MAX_INTENTOS:
        try:
            cantidad = int(input("Introduce la cantidad: "))

            if cantidad <= 0:
                print("Error: la cantidad debe ser mayor que 0.")
            elif cantidad > MAX_CANTIDAD:
                print(f"Error: la cantidad no puede superar {MAX_CANTIDAD}.")
            else:
                return cantidad

        except ValueError:
            print("Error: debes introducir un número entero.")

        intentos += 1

    print("Has superado el máximo de intentos.")
    return None


def pedir_precio():
    """Solicita y valida el precio por unidad."""
    intentos = 0

    while intentos < MAX_INTENTOS:
        try:
            precio = float(input("Introduce el precio por unidad (€): "))

            if precio < 0:
                print("Error: el precio no puede ser negativo.")
            elif precio > MAX_PRECIO:
                print(f"Error: el precio no puede superar {MAX_PRECIO} €.")
            else:
                return precio

        except ValueError:
            print("Error: debes introducir un precio numérico.")

        intentos += 1

    print("Has superado el máximo de intentos.")
    return None


def mostrar_resultado(cantidad, precio, total):
    """Muestra los datos introducidos y el importe calculado."""
    print("\n--- RESUMEN DE LA COMPRA ---")
    print(f"Cantidad de productos: {cantidad}")
    print(f"Precio por unidad: {precio:.2f} €")
    print(f"Importe total: {total:.2f} €")


def main():
    """Controla el funcionamiento principal de la aplicación."""
    print("=== CALCULADORA DE IMPORTES ===")

    cantidad = pedir_cantidad()

    if cantidad is None:
        return

    precio = pedir_precio()

    if precio is None:
        return

    total = calcular_total(cantidad, precio)
    mostrar_resultado(cantidad, precio, total)


# Inicia la aplicación.
if __name__ == "__main__":
    main()

