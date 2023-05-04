import threading as th
import time

print("Hola mundo")
#hksdfhjshd
def paralelo():
    global contador 
    global conti 
    contador = 0
    conti = True
    while conti:
        
        print(contador)
        time.sleep(1)
        contador = contador +1
    print("Fin del Hilo")


print("Inicio del programa principal")
hilo = th.Thread(target=paralelo)
hilo.start()
continuar = True
while continuar:
    dato = input("DIgite algo:")
    if dato == "a":
        print(contador)
    elif dato == "z":
        continuar = False
        conti = False
    else:
        print(dato)
print("Fin del programa principal")
