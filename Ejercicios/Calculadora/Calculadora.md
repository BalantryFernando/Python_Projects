**Calculadora Simple:** Un programa que pida al usuario dos números, y luego le pregunte si quiere 'sumar' o 'restar', y muestre el resultado. (Combina `input`, `int` e `if/elif/else`).
Tengo que crear variables antes de empezar:


## Resultado (abajo):




















numero1 = int(input("Escribe un número: "))
numero2 = int(input("Escribe otro número: "))
accion = input("¿Qué quieres hacer? (escribe 'sumar' o 'restar'): ")

if accion == "sumar":
    print(f"El resultado es: {numero1 + numero2}")
elif accion == "restar":
    print(f"El resultado es: {numero1 - numero2}")
else:
    print("Operación no válida.")