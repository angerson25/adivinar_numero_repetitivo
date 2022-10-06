import random

max=int(input("Hasta que numero quieres adivinar? "))
numero=int(random.uniform(1, max))
eleccion=int(input("\nEscribe tu numero: "))
intentos = 1

while eleccion != numero:
    if eleccion < numero:
        print("El numero es mayor al que digitaste.")

    if eleccion > numero:
        print("El numero es menor al que digitaste.")
    
    eleccion=int(input("Escribe tu numero: "))
    intentos=intentos+1

print("Adivinaste el numero " +str(numero) +  ", en el intento numero " + str(intentos))


