print("BIENVENIDO AL CALCULADOR DE JUBILACIÓN")
nombre= input("Cuál es tu nombre?")
edad = int(input("Ahora dime, cuál es tu edad?"))
if edad <= 65:
    jubilacion = (65 - edad)
    print(f"Muy bien, {nombre}, te faltan {jubilacion} años para jubilarte.")
else: 
    edad>65
    print(f"Ingresa una edad válida, {nombre}.")
    input(int(f"Vuelve a ingresar tu edad"))

"""edad = int(input("¿Cuál es tu edad? "))

if edad >= 18:
    print("Eres mayor de edad. Puedes trabajar en TalentoLab.")
elif edad >= 16:
    print("Podrías realizar una pasantía en TalentoLab.")
else:
    print("Eres demasiado joven para trabajar aquí.")"""

"""contador=0
while contador<8:
    print("Que loco que estoy!")
    contador+=2"""
"""for num in range(1, 101):
    if num % 7 == 0:
        print(f"El número divisible por 7 es: {num}")
        continue"""

