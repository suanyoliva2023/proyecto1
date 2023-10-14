"""
Proyecto integrador parte 3
Para esta sección del proyecto integrador necesitaremos aprender a manipular la terminal:
Iniciar con un número en 0, leer la tecla `n` del teclado en un bucle, por cada presionada, borrar la terminal y e imprimir el nuevo número hasta el número 50.
La operación de borrar la terminal e imprimir el nuevo número debe estar en su propia función. Para borrar la terminal antes de imprimir nuevo contenido usar la instrucción: os.system('cls' if os.name=='nt' else 'clear'), para esto se debe importar la librería os.

"""

from readchar import readkey, key
import os
def borrar_pantalla():
   os.system('cls' if os.name=='nt' else 'clear')
   
def imprimir_numero(contador):
   print(contador)
numero=0
print("Hola, jugador! para jugar preciona la tecla n")
while True: 
    tecla = readkey()
    if tecla == "n":
        borrar_pantalla()
        imprimir_numero(numero)
        if numero == 50:
         print("llegaste a 50, el juego ha terminado!")
         break
        numero = numero + 1
    