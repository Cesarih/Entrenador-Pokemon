print("Bienvenido al mundo pokemon")
genero = input("Eres un niño o una niña? ")

if genero == "niño":
 print("Bienvenido")

else:
 print("Bienvenida")

edad = input("Que edad tienes? ")
if int(edad)<10:
 if genero == "niño":
     print("No tienes edad para ser entrenador")
 else:
    print("No tienes edad para ser entrenadora")
 quit()

print("COMIENZA TU AVENTURA!")
region = input("Necesitaras un compañero de viaje, en que region te encuentras? ")
if region == "Kanto" and genero == "niño":
    print("Tu compañera de viaje es Misty")

else:
    print("Tu compañero de viaje es Brook")

tipo = input("Qué tipo de pokemon quieres para empezar? ")
if tipo == "agua":
    print("Tu starter es Oshawott")

elif tipo == "fuego":
    print("Tu starter es Cyndaquil")

else:
    print("Tu starter es Rowlet")