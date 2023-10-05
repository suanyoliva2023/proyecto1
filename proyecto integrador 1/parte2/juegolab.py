#Escribir un programa que corra un bucle infinito leyendo e imprimiento las teclas y sólo terminará cuando se presione la tecla ↑ indicada como UP
from readchar import readkey, key

print("Bienvenido al juego")
print("para terminar el juego presionar la Siguiente tecla ↑")

while True: 
    tecla = readkey()
    if tecla == key.UP:
     print("Para terminar el juego tocar la tecla UP")
     break
    print("presione la tecla")

  

