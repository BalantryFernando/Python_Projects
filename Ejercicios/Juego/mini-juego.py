numero_secreto = int(7)
#Numero usuario como tal necesita un valor, le daremos el 0
numero_usuario = int(0)

while numero_usuario != numero_secreto:
    numero_usuario = int(input("Escribe un numero: "))
    if numero_usuario > numero_secreto:
        print("Demasiado alto")
    elif numero_usuario < numero_secreto:
        print("Demasiado pequeño")
print(f"{numero_secreto} es el numero correcto!!")