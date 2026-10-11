try:
    numero= int("Hola")
except ValueError :
    print("El valor ingresado no es válido")
    #Esto es para mensajes de errores, en este caso except maneja ese error específico, pasar a 
    #entero un string

try:
    numero= int(input("Ingrese el número"))
    result= 10/numero
except ValueError:
    print ("Debe ingresar un número")
    #por ejemplo ahí ingresó una letra
except ZeroDivisionError :
    print("No se puede dividir por 0")
finally:
    print("Proceso finalizado")


diccio={
        "nombre":"Lalo",
        "sexo":"Masc"
    }

try:
    print(diccio["dni"])
except KeyError:
    print("El valor NO está definido")