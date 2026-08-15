import re

print("Escribe tu nombre y el año en el que naciste")
escrito = str(input(">"))

resultado_numero = re.search(r"\d{4}", escrito)
# La función SEARCH, guardara el resultado en su argumento group
valor_coincidido = resultado_numero.group(0)

resultado_a_letra = re.search(r"\w+", escrito)
valor_letra_coincidido = resultado_a_letra.group(0)

# EL 1 imprime el primer ""
print(f"Te llamas {valor_letra_coincidido}")
print(f"Entonces tienes {valor_coincidido} años")