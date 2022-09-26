#El ordenador advina nuestro numero
#El ordenador debe adivinar el número seleccionado por el jugador al llamar la funcion.


import random


print(''' 


▒█▀▀█ █░░█ █▀▀ █▀▀ █▀▀ 　 ▀▀█▀▀ █░░█ █▀▀ 　 █▀▀▄ █░░█ █▀▄▀█ █▀▀▄ █▀▀ █▀▀█ 
▒█░▄▄ █░░█ █▀▀ ▀▀█ ▀▀█ 　 ░░█░░ █▀▀█ █▀▀ 　 █░░█ █░░█ █░▀░█ █▀▀▄ █▀▀ █▄▄▀ 
▒█▄▄█ ░▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ 　 ░░▀░░ ▀░░▀ ▀▀▀ 　 ▀░░▀ ░▀▀▀ ▀░░░▀ ▀▀▀░ ▀▀▀ ▀░▀▀

    ''')

def computer_guess(number):
    print(f'Escriba el rango de numero a adivinar que sera desde el 1 hasta {number} . La computadora intentara adivinar\n\n')
    
    #intervalos de valores
    limite_inferior = 1
    limite_superior = number

    user_input = ""


    #pedir repuesta al usuario usaremos while para predecir el numero seleccionado del usuario
    while user_input != "c":
        #generar prediccion
        if limite_inferior != limite_superior:
            prediccionPCU = random.randint(limite_inferior,limite_superior)
        else:
            prediccionPCU = limite_inferior #tb puede ser el limite inferior
        
        #Obtener feedback del usuario para ayudar a adivinar el numero a la compu y convertirlo en mayuscula
        user_input = input(f'El numero que adivino el CPU es: {prediccionPCU}\n- si es muy alta, ingresa (A)\n- si es baja, ingresa (B)\n- si es correcta ingresa (C)\n  ').lower()

        if user_input =="a":
            limite_superior = prediccionPCU-1
        elif user_input == "b":
            limite_inferior = prediccionPCU +1
    print(f'!!CPU has guess your number. It was:  {number}') #terminamos con el loop


computer_guess(15) #Quiero adivinar el 9


