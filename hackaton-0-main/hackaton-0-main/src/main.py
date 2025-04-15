def calculadora(num1, num2 , operacion):
    while True:
        
        try:
            
            if operacion == "+":
                resultado = num1 + num2
            elif operacion == "-":
                resultado = num1 - num2
            elif operacion == "*":
                resultado = num1 * num2
            elif operacion == "/":
                if num2 == 0:
                    print("Error: No se puede dividir entre cero.")
                    continue
                resultado = num1 / num2
            else:
                print("Operación no válida. Intenta nuevamente.")
                continue

            print(f"Resultado: {resultado}")

            
            otra = input("¿Deseas hacer otra operación? Responde un (si)").lower()
            if otra != "si":
                print("Gracias por usar la calculadora.")
                break

        except ValueError:
            print("Entrada inválida. Por favor ingresa números válidos.")

num1 = float(input("ingrese un numero"))
num2 = float(input("Ingrese otro numero"))
operacion = str(input("Ingrese operación"))

calculadora(num1 , num2, operacion)
