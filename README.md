## Bienvenidos a mi primer repositorio de practicas 😄

**Para este repositorio utilice:**

*Cmder*, *Visual studio code*  *y Git*

##### COMANDOS BASICOS DE CMDER:

cd: sirve para moverme a una carpeta deseada ejemplo "cd documentos" y para ir hacia atras se usa "cd .."

ls: listado de carpetas y archivos dentro de un directorio

mkdir: crear directorios nuevos (carpetas)

touch: crear archivos dentro de un directorio

crtl+l: limpias la consola

##### COMANDOS DE PYTHON USADOS:

Print() este comando sirve para escribir una indicación en el sistema de programación, v.g. cuando pide una introducción de variables numéricas. También es para mostrar resultados.

Cuando se quiere escribir un texto se debe de escribir con comillas, así

Print(“Buenos días”)

Int() este comando es utilizado para que Python tome la entrada como un número entero.

Input() este comando es usado para obtener una respuesta por parte del usuario que está usando el programa. Si no introduce números se marcará un error.

float() interpreta la entrada como un número decimal. Si no introduce números se marcará un error.

##### CONDICIONALES DE PYTHON:

if: if opcion == 1. Aquí, si lo “traducimos”, sería“Si el usuario elige la opción 1, entonces…” y luego viene todo el código por debajo que conocemos como bloque de código.

else: si se desea ejecutar otro código en caso de que no se cumpla el if. Ósea, si por ejemplo, el usuario no elige la opción 1, entonces (else)…

elif: se utiliza cuando utilizamos múltiples condiciones, lo que en el código de esta clase son la opción 2 y 3. Teníamos la opción 1, pero debemos también evaluar qué pasa si el usuario elige la opción 2 o 3, por lo que decimos “que estamos evaluando múltiples condiciones”.

##### COMENTARIOS EN PYTHON:

Para realizar un comentario (de una sola línea), utilizamos el “#”. Un comentario es simplemente texto, el cual no es ejecutado y no afecta en absoluto en el código. Se utiliza para explicar las líneas de código

##### METODOS PARA TRABAJAR CON TEXTO EN PYTHON

variable.strip(): El método strip eliminará todos los caracteres vacíos que pueda contener la variable

variable.lower(): El método lower convertirá a las letras en minúsculas.

variable.upper(): El método upper convertirá a las letras en mayúsculas.

variable.capitalize(): El método capitalize convertirá a la primera letra de la cadena de caracteres en mayúscula.

variable.replace (‘o’, ‘a’): El método replace remplazará un caracterer por otro. En este caso remplazará todas las ‘o’ por el caracter ‘a’.

len(variable): Te indica la longitud de la cadena de texto dentro de la variable en ese momento.

##### COMO USAR SLICES EN PYTHON:

nombre = "Francisco"
nombre
"Francisco"
nombre[0 : 3)
Arranca desde el primer índice hasta llegar antes del 3° índice.
El resultado sería
"Fra"

nombre[:3]
Va desde el principio hasta antes de llegar del 3° índice. Como no hay ningún parámetro en el primer lugar, se interpreta que arranca desde el principio. Recordemos que empezamos a contar desde cero como primer dígito.
El resultado sería
"Fra"

nombre[1:7]
Arranca desde el índice 1 hasta llegar antes del 7.
El resultado sería
"rancis"

nombre[1:7:2]
Arranca desde el índice 1 hasta llegar antes del 7, pero pasos de 2 en 2, ya que eso es lo que nos indica el 3er parámetro, el cual es 2.
El resultado sería
"rni"

nombre[1::3]
Arranca desde el índice 1 hasta el final del string (al no haber ningún 2° parámetro, significa que va hasta el final), pero en pasos de 3 en 3.
El resultado sería
"rcc"

nombre[::-1]
Al no haber parámetro en las 2 primeras posiciones, se interpreta que se arranca desde el inicio hasta el final, pero en pasos de 1 en 1 con la palabra al revés, porque es -1.
El resultado sería
"ocsicnarF"

##### BUCLE WHILE:

Un bucle while permite repetir la ejecución de un grupo de instrucciones mientras se cumpla una condición (es decir, mientras la condición tenga el valor True).

La sintaxis del bucle while es la siguiente:

while condicion:
    cuerpo del bucle
Python evalúa la condición:

Si el resultado es True, se ejecuta el cuerpo del bucle. Una vez ejecutado el cuerpo del bucle, se repite el proceso (se evalúa de nuevo la condición y, si es cierta, se ejecuta de nuevo el cuerpo del bucle) una y otra vez mientras la condición sea cierta.
Si el resultado es False, el cuerpo del bucle no se ejecuta y continúa la ejecución del resto del programa.

##### COMO TRABAJAR CON LISTAS EN PYTHON:

Declarar lista:

my_lista = []
my_lista = list()

Unir listas:
my_lista = [1]
my_lista2 = [2,3,4]
my_lista3 = my_lista + my_lista2
my_lista3 # [1,2,3,4]

Partir listas como slices:

my_lista = [1,2,3]
my_lista[1:] = [2,3]

Extender una lista:

my_lista = [1]
my_lista2 = [2,3,4]
my_lista.extend(my_lista2) # [1,2,3,4]

Multiplicar listas:
my_lista = ['a']
my_lista2 = my_lista * 5
my_lista2 # ['a','a','a','a','a']

Eliminar el último elemento de la lista:

my_lista = [1,2,3,4,5]
my_lista = my_lista.pop()
my_lista # [1,2,3,4]

Ordenar lista:

my_lista = [2,1,5,4,3]
my_lista = my_lista.sort()
my_lista # [1,2,3,4,5]

Eliminar un elemento:

my_lista = [1,2,3,4,5]
del my_lista[0]
my_lista # [2,3,4,5]

Eliminar si conocemos su valor:

my_lista = [1,2,3,4,5]
my_lista.remove(3)
my_lista #[1,2,4,5]

Saber qué métodos hay dentro de un elemento:

my_lista = [1,2,3,4,5]
dir(my_lista) # ['__add__', '__class__', '__contains__', ...

Modificar un elemento:

my_lista = [1,2,3,4,5]
my_lista[0] = 100
my_lista # [100,2,3,4,5]

Añadir un elemento al final:

my_lista = [1,2,3,4,5]
my_lista.append(6)
my_lista # [1,2,3,4,5,6]

Organizar una lista:

my_lista = [2,5,1,3,4]
my_lista.sort() #[1,2,3,4,5]

Métodos adicionales para listas:

.sorted()
También ordena como sort() pero modifica la lista inicial

.clear()
Vacía la lista

.count()
Cuenta las veces que esta un elemento en lista

.index()
Indica la posición donde esta un elemento de la lista

.insert()
Inserta un elemento en una posición dada ej: lista.insert(posición,item)

.reverse()
Le da la vuelta a una lista

##### COMO TRABAJAR CON TUPLAS EN PYTHON:

Las tuplas son estructuras de datos inmutables. Es decir, no puedes modificar una tupla a agregando o quitando un valor. Lo único que puedes hacer es definir de nuevo esa tupla a. Los objetos inmutables (como los strings) son tipos de datos para Python que apuntan a un lugar específico en memoria y que su contenido no puede ser cambiado. Al cambiar el contenido predefiniendo el contenido de la variable a, entonces cambiará su posición en memoria.

Declarar tupla

mi_tupla = ()
mi_tupla = (1,2,3)

Generar una tupla de 1 solo valor
La , es obligatoria.
mi_tupla = (1,)

Acceder a un índice de la tupla
mi_tupla = (1,2,3)
mi_tupla[0] #1
mi_tupla[1] #2
mi_tupla[2] #3

Reasignar una tupla
mi_tupla = (1,2,3)
mi_otra_tupla = (4,5,6)
mi_tupla =+ mi_otra_tupla

Métodos para trabajar con tuplas
Usando el ejemplo:

mi_tupla = (1,1,1,2,2,3)
Encontraremos los siguientes métodos:

mi_tupla.count(1)
Devolverá 3, ya que el número 1 aparece 3 veces en la tupla.

mi_tupla.index(3)
Devolverá 5, índice de la primera instancia donde se encuentra un elemento.

mi_tupla.index(1)
Devolverá 0

mi_tupla.index(2)
Devolverá 3.

