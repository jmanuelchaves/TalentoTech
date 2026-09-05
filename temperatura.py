sensores_altos = 0
temperatura_total=0
medidor_temperatura=0

while True:
    temperatura= (input("Ingrese la temperatura: (salir para sacar el programa)"))
    

    if temperatura == ("salir"):
        break

    temperatura = float(temperatura)
    temperatura_total = float(temperatura_total)
    medidor_temperatura = float(medidor_temperatura)

    temperatura_total += temperatura

    medidor_temperatura+=1

    if temperatura < -10:
        print("El sensor está midiendo mal")
        continue

    if temperatura >=43:
        print("TEMPERATURA EXTREMA!!!!!!!")
        print("DETENER SERVIDORES")
        break

    if temperatura >=33:
        print("La temperatura es demasiado alta") 
        sensores_altos += 1
    elif temperatura < 25:
        print("La temperatura es moderada")
    elif temperatura <=10:
        print("La temperatura es fría")
    else: print("La temperatura es normal")



print(f"Se registraron {sensores_altos} sensores de temperatura ALTA") 
print(f"La temperatura promedio fue: {int(temperatura_total/medidor_temperatura)}")
