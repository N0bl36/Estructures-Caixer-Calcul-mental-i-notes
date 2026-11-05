import time
numeroNotas= int(input("Introduce el número de notas que deseas ingresar: "))
numeroRepeticiones=0
aprobados=0
suspendidos=0
media=0
maximo=0
minimo=10
while numeroRepeticiones < numeroNotas:
    nota= float(input("Introduce la nota: "))
    if nota < 0 or nota > 10:
        print("Nota no válida. Introduce una nota entre 0 y 10.")
    elif nota >= 5:
        aprobados+=1
        numeroRepeticiones+=1
        if nota > maximo:
            maximo=nota
    elif nota < 5:
        suspendidos+=1 
        numeroRepeticiones+=1
        if nota < minimo:
            minimo=nota
    media+=nota
    
    
    time.sleep(0.5)

print("-------------------------------")
print("Número de aprobados:", aprobados)
print("Número de suspendidos:", suspendidos)
print("La media de las notas es:", media/numeroNotas)
print("La nota máxima es:", maximo)
print("La nota mínima es:", minimo)
print("-------------------------------")