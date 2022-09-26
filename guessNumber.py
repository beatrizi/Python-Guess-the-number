'''
module implements pseudo-random number generators for various distributions.
https://docs.python.org/3/library/random.html
Functions for integers:: random.randint(a, b)
Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).
'''

# El usuario adivina el número aleatorio generado por la computadora.
# Import : bring a MODULO o LIBRARY -file-  of python that have functionso and other elements to use in a program
import random

print(''' 


▒█▀▀█ █░░█ █▀▀ █▀▀ █▀▀ 　 ▀▀█▀▀ █░░█ █▀▀ 　 █▀▀▄ █░░█ █▀▄▀█ █▀▀▄ █▀▀ █▀▀█ 
▒█░▄▄ █░░█ █▀▀ ▀▀█ ▀▀█ 　 ░░█░░ █▀▀█ █▀▀ 　 █░░█ █░░█ █░▀░█ █▀▀▄ █▀▀ █▄▄▀ 
▒█▄▄█ ░▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ 　 ░░▀░░ ▀░░▀ ▀▀▀ 　 ▀░░▀ ░▀▀▀ ▀░░░▀ ▀▀▀░ ▀▀▀ ▀░▀▀

    ''')

def guess(max_number):
    #max_number is going be the range of number to guess
    print("Guess the number that the computer has choosen")
  

    computer_number = random.randint(1, max_number) # número aleatorio entre 1 y max_number, inclusive.En parentesis ponenemos 2 parametros.

    # La user_prediction es 0 inicialmente para que no coincida con el número aleatorio. 
    user_prediction = 0  # cero sera diferente a computer_number

    # Continuar prediciendo el número hasta que la user_prediction sea correcta.
    # No sabemos cual sera el numero de iteraciones

    while user_prediction != computer_number:
        # El usuario ingresa un número.
        # cualquier valor que ingresa sera una cadena de caracteres y en este caso hay que catear
        user_prediction = int(input(f'Adivina un número entre 1 y {max_number}: ')) #type F-string
        # Si el número es menor que el número aleatorio, se 
        # muestra un mensaje.
        if user_prediction < computer_number:
            print('Try again. The number you are writing is small than the number I am thinking.')
        # Si el número es mayor que el número aleatorio, se
        # muestra un mensaje.
        elif user_prediction > computer_number:
            print('Try again. The number you are writing too big than the number I am thinking.')

    # El ciclo o bucle se detiene cuando el usuario adivina el número
    # correctamente y se muestra un mensaje final.
    print(f'Congratulations! you guess my number{computer_number}.')


# Llamar a la función
guess(10)