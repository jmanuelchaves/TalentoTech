

print ("¡Hola Automation Tester!")
nombre=str(input("¿Cuál es tu nombre?"))

def saludar(nombre):
    print(f"¡Hola {nombre}!")

saludar(nombre)


print("SEGUNDA FUNCIÓN CON RETURN")

def suma(numero1=3, numero2=4):
    resultado=numero1+numero2
    return resultado

doble= suma()*2

print(doble)