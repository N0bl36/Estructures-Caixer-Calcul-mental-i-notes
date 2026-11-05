import random
import time
correctos=0
for i in range(5):
    numero1= random.randint(1, 10)
    numero2= random.randint(1, 10)
    resultado= numero1 + numero2
    time.sleep(0.5)
    print("cuanto es", numero1, "+", numero2, "?")
    time.sleep(0.5)
    respuesta= int(input("Tu respuesta: "))
    time.sleep(0.5)
    if respuesta == resultado:
        print("Correcto")
        correctos+=1
    else:
        time.sleep(0.5)
        print("Incorrecto. La respuesta correcta es: ", resultado)
time.sleep(0.5)
if correctos == 5:
    print("Excle·lent")
elif correctos >= 4:
    print("Molt bé")
else:
    print("Has de practicar més")
