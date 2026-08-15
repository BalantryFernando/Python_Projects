


#LOGICA HUMANO-PYTHON, ENTENDERLO ESTARIA BIN

def mostrar_lista(lista_de_tareas):
    print("\n--- TUS TAREAS ---")
    contador = 1
    for tarea in lista_de_tareas:
        print(f"{contador}. {tarea}")
        contador = contador + 1
    print("------------------\n")