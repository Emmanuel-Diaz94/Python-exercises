import random 

print("juego piedra, papel o tijera")
print("opciones")
print("1- piedra, 2- papel, 3- tijera")
option_user = int(input("elige la opcion con la quieras jugar:"))

#Si el usuario escribe un numero menor a 1 y mayor a 3, le volver a pedir que ingrese uno correcto
if option_user > 3 and option_user < 1 :
    print("Esa no es una option valida")
    option_user = int(input("vuelve a elegir la opcion con la quieras jugar:"))
else:
    #generamos numeros aleatorios entre 1 y 3
    random_number = random.randint(1, 3)

    #convertimos la opcion de la maquina en piedra papel o tijeras
    if random_number == 1:
        random_option = "piedra"
        random_option_icon = "📄"
    elif random_number == 2:
        random_option = "papel"
        random_option_icon = "📄"
    else:
        random_option = "tijeras"
        random_option_icon = "✂️"

   #convertimos la opcion del usuario en piedra papel o tijeras
    if option_user == 1:
        option_user_play = "piedra"
        option_user_play_icon = "📄"
    elif option_user == 2:
        option_user_play = "papel"
        option_user_play_icon = "📄"
    else:
        option_user_play = "tijeras"
        option_user_play_icon = "✂️"
 
    
    if random_option == option_user_play:
        print("es un empate")
        print("tu haz elegido " + option_user_play + option_user_play_icon)
        print("la maquina eligio " + random_option + random_option_icon)
    else:
        print("luego veremos quien gano")
        print("tu haz elegido " + option_user_play + option_user_play_icon)
        print("la maquina eligio " + random_option + random_option_icon)