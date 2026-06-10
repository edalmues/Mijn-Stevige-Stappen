def calculadora():
    while True:
        print("1. SUMAR")
        print("2. RESTA")
        print("3. MULTIPLICACIÓN")
        print("4. DIVISIÓN")
        print("5. SALIR")

        option = int(input("Ingrese una opcion: "))

        match option:
            case 1:
                num1 = int(input("Ingrese un número: "))
                num2 = int(input("Ingrese un número: "))
                suma = num1 + num2
                print("Resultado suma: " + str(suma))
            case 2:
                num1 = int(input("Ingrese un número: "))
                num2 = int(input("Ingrese un número: "))
                resta = num1 - num2
                print("Resultado resta: " + str(resta))
            case 3:
                num1 = int(input("Ingrese un número: "))
                num2 = int(input("Ingrese un número: "))
                multiplicación = num1 * num2
                print("Resultado multiplicación: " + str(multiplicación))
            case 4:
                num1 = int(input("Ingrese un número: "))
                num2 = int(input("Ingrese un número: "))

                if num2 == 0:
                    print("ERROR. No se puede dividir por 0")
                    continue 
                división = num1 / num2
                print("Resultado de la división: " + str(división))
                
            case 5:
                print("Saliendo del sistema.... que la fuerza te acompañe.")
                break
print(calculadora())