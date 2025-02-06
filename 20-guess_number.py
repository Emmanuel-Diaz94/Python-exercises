import random

secret_number = random.randint(1,10)

print("estoy pensando en un numero entre el 1 y el 10 adivina cual es")

while True: 
    attempts = int(input("ingresa el numero:"))

    if attempts < secret_number:
        print("El numero es muy bajo intenta de nuevo")
    elif attempts > secret_number:
        print("el numero es muy alto intente de nuevo")
    else:
        print("felicidades adivinaste el numero") 
        Break
