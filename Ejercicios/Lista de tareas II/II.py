# Defines la variable de grupo
objetos = []
# Creación de la variable acción
ver = "ver"

while True:
    escrito = input("Escribe algo para la lista (o'fin') para terminar :")

# Rotura de bucle
    if escrito == "fin":
        break
# En caso que no se rompa continua
    # Si es ver
    elif escrito == "ver":        
        print(objetos)
    else:
        objetos.append(escrito)
# En caso de que no pase: Agrega lo escrito a la lista objet
    
print("Tu lista final es: ")
print(objetos)

