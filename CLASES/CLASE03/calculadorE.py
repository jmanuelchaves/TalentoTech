from calculfunciones import *

def calculadora ():
    print ("***BIENVENIDO A CALCULADORA***")
    a = float(input("Ingrese primer número y presione ENTER "))
    b = float(input("Ingrese segundo número y presione ENTER "))
    print("ELIJA UNA OPCIÓN DE OPERACIÓN")
    opcion = input("1)Sumar 2)Restar 3)Dividir 4)Multiplicar ")

    try:
        if opcion == '1': 
            resultado = sumar(a,b)
        elif opcion == '2':
            resultado = restar(a,b)
        elif opcion == '3':
            resultado = dividir(a,b)
        elif opcion == '4':
            resultado = multiplicar(a,b)
        else:
            print("Opción Inválida")
            return
        print (f"Resultado:{resultado}")
        
    except ValueError as e:
        print(f"Error{e}")

calculadora()