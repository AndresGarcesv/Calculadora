from operaciones import suma, resta, multiplicacion, division, potencia, division_entera

def obtener_numeros():
    """Solicita y valida dos números al usuario."""
    while True:
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            return num1, num2
        except ValueError:
            print("Error: Por favor ingrese números válidos.")

def main():
    print("Calculadora Modular")
    print("Operaciones disponibles: +, -, *, /, **, //")
    
    while True:
        try:
            # Obtener números
            num1, num2 = obtener_numeros()
            
            # Obtener operador
            operador = input("Ingrese el operador (o 'q' para salir): ").strip()
            
            if operador.lower() == 'q':
                print("Saliendo de la calculadora...")
                break
            
            # Realizar operación según el operador
            if operador == '+':
                resultado = suma(num1, num2)
            elif operador == '-':
                resultado = resta(num1, num2)
            elif operador == '*':
                resultado = multiplicacion(num1, num2)
            elif operador == '/':
                try:
                    resultado = division(num1, num2)
                except ZeroDivisionError as e:
                    print(f"Error: {e}")
                    continue
            elif operador == '**':
                resultado = potencia(num1, num2)
            elif operador == '//':
                try:
                    resultado = division_entera(num1, num2)
                except ZeroDivisionError as e:
                    print(f"Error: {e}")
                    continue
            else:
                print("Error: Operador no válido")
                continue
            
            # Mostrar resultado
            print(f"Resultado: {num1} {operador} {num2} = {resultado}")
            
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    main()