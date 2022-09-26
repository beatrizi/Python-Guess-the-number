#El ordenador advina nuestro numero



import random


print(''' 


▒█▀▀█ █░░█ █▀▀ █▀▀ █▀▀ 　 ▀▀█▀▀ █░░█ █▀▀ 　 █▀▀▄ █░░█ █▀▄▀█ █▀▀▄ █▀▀ █▀▀█ 
▒█░▄▄ █░░█ █▀▀ ▀▀█ ▀▀█ 　 ░░█░░ █▀▀█ █▀▀ 　 █░░█ █░░█ █░▀░█ █▀▀▄ █▀▀ █▄▄▀ 
▒█▄▄█ ░▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ 　 ░░▀░░ ▀░░▀ ▀▀▀ 　 ▀░░▀ ░▀▀▀ ▀░░░▀ ▀▀▀░ ▀▀▀ ▀░▀▀

    ''')

def computer_guess(number):
    print(f'Escriba el rango de numero a adivinar que sera desde el 1 hasta {number} . La computadora intentara adivinar')
    
    #intervalos de valores
    limite_inferior = 1
    limite_superior = number

    user_input = ""


