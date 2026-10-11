print("#"*10, "BIENVENIDO A CALCULADORA AVANZADA","#"*10)




while True:
    numero1=float(input("Ingrese el primer número "))
    print("OPCIONES PARA OPERAR")
    print("1.Sumar")
    print("2.Restar")
    print("3.Multiplicar")
    print("4.Dividir")
    print("5.Salir")
    op=input("Seleccione una opción ").upper()


    match op:

        case "1": 
            numero2=float(input("Ingrese el segundo número "))
            resultado=numero1+numero2
            print("Su resultado es: ", (resultado))
        case "2":
            numero2=float(input("Ingrese el segundo número "))
            resultado=numero1-numero2
            print("Su resultado es: ", (resultado))
        case "3":
            numero2=float(input("Ingrese el segundo número ")) 
            resultado=numero1*numero2
            print("Su resultado es: ", (resultado))
        case "4":
            numero2=float(input("Ingrese el segundo número ")) 
            resultado=numero1/numero2
            print("Su resultado es: ", (resultado))
        case "5": 
            print("Gracias por participar")
            break
        case _:
            print("Por favor ingrese una opción válida")
            continue






