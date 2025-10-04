# Defines la variable de grupo
objeto = []
# Creación de bucle infinito, termina desde dentro
while True:
    escrito = input("Escribe algo para la lista (o'fin') para terminar :")

# Rotura de bucle
    if escrito == "fin":
        break
# En caso que no se rompa continua
    objeto.append(escrito)

print("Tu lista final es: ")
print(objeto)
