numero_escrito1 = input("Escribe un numero :")
numero1 = int(numero_escrito1)

numero_escrito2 = input("Escribe un numero :")
numero2 = int(numero_escrito2)

sumar = "sumar"
restar = "restar"
acción_escrita = input(f"{sumar} o {restar} :")

if acción_escrita == sumar:
    print(numero1 + numero2)
elif acción_escrita == restar:
    print(numero1 - numero2)
else:
    print("Escribe sumar o restar en minusculas")