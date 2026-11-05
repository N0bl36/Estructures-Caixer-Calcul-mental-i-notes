import time
import random
eleccionSaldo=random.choice([100, 110, 120, 130])
saldo=eleccionSaldo
eleccionTecla=0
contador=0
while eleccionTecla != 4:
    print("1= Consultar saldo")
    print("2= Ingresar diners")
    print("3= Retirar diners")
    print("4= Sortir del programa")
    eleccionTecla=int(input("Elije que operación hacer: "))
    if eleccionTecla == 1:
        time.sleep(0.5)
        print("Tu saldo actual es: ", saldo)
        contador+=1
        time.sleep(0.5)
    elif eleccionTecla == 2:
        time.sleep(0.5)
        cantidad=int(input("Introduce la cantidad a ingresar: "))
        time.sleep(0.5)
        if cantidad <= 0:
            print("No puedes ingresar una cantidad negativa o cero.")
        else:
            saldo+=cantidad
            contador+=1
        cantidad=0
    elif eleccionTecla == 3:
        time.sleep(0.5)
        cantidad=int(input("Introduce la cantidad a retirar: "))
        time.sleep(0.5)
        if cantidad > saldo:
            print("No puedes retirar una cantidad mayor a tu saldo actual.")
        elif cantidad <= 0:
            print("No puedes retirar una cantidad negativa o cero.")
        else:
            saldo-=cantidad
            contador+=1
        cantidad=0
    elif eleccionTecla == 4:
        time.sleep(0.5)
        print("Saliendo del programa, has realizado ", contador, " operaciones.")
    else:
        time.sleep(0.5)
        print("Opción no válida. Por favor, elige una opción del 1 al 4.")