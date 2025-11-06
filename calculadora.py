def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    return a / b

def main():
    print("=== Calculadora de Christopher Daniel Jimenez Bautista ===")
    print("Operaciones disponibles: suma, resta, multiplicacion, division")

    while True:
        op = input("Ingresa operación (o 'salir' para terminar): ").strip().lower()
        if op == "salir":
            print("¡Hasta luego!")
            break

        try:
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
        except ValueError:
            print("Por favor, ingresa números válidos.")
            continue

        if op == "suma":
            print("Resultado:", sumar(a, b))
        elif op == "resta":
            print("Resultado:", restar(a, b))
        elif op == "multiplicacion":
            print("Resultado:", multiplicar(a, b))
        elif op == "division":
            print("Resultado:", dividir(a, b))
        else:
            print("Operación no válida. Intenta nuevamente.")

if __name__ == "__main__":
    main()
