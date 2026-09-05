print("BIENVENIDO A CALCULADORA")
while True:
    num1=float(input("Ingrese el primer número: "))
    num2=float(input("Ingrese el segundo número: "))

    print("Ingrese la operación que desea realizar: +, -, *, /, para salir presione cualquier tecla")
    operacion=input("Operación: ")
    if operacion=="+":
        resultado=num1+num2
    elif operacion=="-":
        resultado=num1-num2
    elif operacion=="*":
        resultado=num1*num2
    elif operacion=="/":
        resultado=num1/num2
    else:
        print("Operación no válida")
        break
    print("El resultado es: ", resultado)