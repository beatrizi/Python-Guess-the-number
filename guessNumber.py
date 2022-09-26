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
    print("Guess the number that the computer has choose")
  

    computer_number = random.randint(1, max_number) # número aleatorio entre 1 y max_number.

    # La predicción es 0 inicialmente para que no coincida con el número aleatorio. 
    predicción = 0

    # Continuar prediciendo el número hasta que la predicción sea correcta.
    while predicción != computer_number:
        # El usuario ingresa un número.
        predicción = int(input(f'Adivina un número entre 1 y {max_number}: '))
        # Si el número es menor que el número aleatorio, se 
        # muestra un mensaje.
        if predicción < computer_number:
            print('Intenta otra vez. Este número es muy pequeño.')
        # Si el número es mayor que el número aleatorio, se
        # muestra un mensaje.
        elif predicción > computer_number:
            print('Intenta otra vez. Este número es muy grande.')

    # El ciclo o bucle se detiene cuando el usuario adivina el número
    # correctamente y se muestra un mensaje final.
    print(f'¡Felicitaciones! Adivinaste el número {computer_number} correctamente.')

# Llamar a la función
guess(10)