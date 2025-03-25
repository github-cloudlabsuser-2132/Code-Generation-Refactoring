

def calculadora():
    print("Bienvenido a la calculadora básica")
    print("Selecciona una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    while True:
        try:
            opcion = int(input("Ingresa el número de la operación (1/2/3/4): "))
            if opcion not in [1, 2, 3, 4]:
                print("Por favor, selecciona una opción válida.")
                continue

            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))

            if opcion == 1:
                print(f"El resultado de la suma es: {num1 + num2}")
            elif opcion == 2:
                print(f"El resultado de la resta es: {num1 - num2}")
            elif opcion == 3:
                print(f"El resultado de la multiplicación es: {num1 * num2}")
            elif opcion == 4:
                if num2 == 0:
                    print("Error: No se puede dividir entre cero.")
                else:
                    print(f"El resultado de la división es: {num1 / num2}")

            otra = input("¿Quieres realizar otra operación? (s/n): ").lower()
            if otra != 's':
                print("Gracias por usar la calculadora. ¡Adiós!")
                break
        except ValueError:
            print("Entrada no válida. Por favor, ingresa números válidos.")

# Llamar a la función calculadora
calculadora()