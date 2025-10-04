Ejemplos, con mini-explicación:


## Movimientos importantes

numero_texto = input("Dime un numero: ")
	Captura lo que se escriba en INT
	
numero_real = int(numero_texto)
	Lo capturado en STRING se guarda y convierte en INT
		**Se declara la variable literalmente**

print("--- TUS TAREAS ---") Imprime un titulo limpio
print("------------------") Imprime un final limpio
## Bucles:

for **variable_temporal** in **variable** --> se repetira tantas veces haigan elementos en la lista amigos

for **i** in range(**n**) --> repite esto **n** veces
	*codigo*

if **variable_input** == "variable" --> Si la variable_input es igual a la variable, entonces suecede esto
	código

while no lo entiendo
Crear un bucle while que se repita mientras el numero_usuario sea diferente (!=) al numero_secreto.


## Guardar variables

nombre = "Fernando" --> STRING
edad = 20 --> INTEGER
input() --> Detiene el programa para capturar lo que se escriba STRING
	
###### Listas
compras = ["leche", "pan", "huevos"]
	Python tiene en cuenta los valores desde 0
			compras[1] -->Python se lo toma como una operación
			**Hay 3, pero se cuenta desde 0-1-2**
			
Para añadir un elemento al final se usa **append()**
compras.append("zumo")

## Logica Condicional

if ...condición... --> Si pasa esto
	Ejecuta esto

elif ...condición... --> Si el if no pasa lo primero
	Ejecuta esto

else ...condición... --> Si ni uno ocurre, haz esto
	Ejecuta esto

![[Pasted image 20251001085350.png]]


## Definición

def resta(numero1, numero2):
    return numero1 + numero2

Entonces, esta "def" podremos usarla en:
def(12, 5)
	Entonces realiza el "def"

Podemos guardar 
variable = resta(12, 5) cual posteriormente usandolo, imprimirá el resultado

* Conversión humano-python

¿Si python empiza a contar desde 0-1-2 y los humanos desde 1-2-3?

