# Reto 01

### Reto 1.1
Crear una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, según la elección del usuario, la forma de entrada de la función será los dos operandos y el caracter usado para la operación. entrada: (1,2,"+"), salida (3).

```python


def calculos(numero1, numero2, operacion):
    if operacion == "+": 
        return numero1 + numero2
    elif operacion == "-":
        return numero1 - numero2
    elif operacion == "*":
        return numero1 * numero2
    elif operacion == "/":
        if numero2 !=0: 
            return numero1 / numero2
        else:
            print("La división por cero no es posible")
    else: 
        print("La operación no es válida")

numero1 = float(input("Por favor ingresa el primer número a operar: "))
operacion = input("Por favor selecciona la operación (+, -, *, /): ")
numero2 = float(input("Por favor ingresa el segundo número a operar: ")) 
       
    
resultado = calculos(numero1, numero2, operacion) 

if resultado is not None: 
  print(f"El resultado de {numero1} {operacion} {numero2} es {resultado}") 
  
  ```

 En primer lugar se solicita al usuario que digite la operación  los números deseados. Dentro de la función, se comparan los datos ingresados como strings con otros strings establecidos, en caso de ser iguales, se debe realizar la respectiva operación entre los números. En caso de que el usuario quiera dividir entre 0 el programa aclara que no es posible, y en caso de ingresar una operación invalida (símbolo de operación o números erróneos) el programa envía un mensaje de error.
### Reto 1.2
Realice una función que permita validar si una palabra es un palíndromo. Condición: No se vale hacer slicing para invertir la palabra y verificar que sea igual a la original.

```python
palabra = input("Ingrese su palabra aquí: ")

def detecta_palindromo(palabra):
    palabra = palabra.lower()  
    inicio = 0 
    final = len(palabra)-1 
    
    while inicio < final: 
        if palabra[inicio] != palabra[final]: 
            return False 
        inicio += 1 #Se comparan índices, si son iguales, se compara el segundo con el penúltimo. 
        final -= 1 #Se recorre la palabra completa, letra por letra, verificando si hay coincidencias
        
    return True 

if detecta_palindromo(palabra):
    print("Es palíndromo")
else: 
    print("No es palíndromo")
```
Con la palabra ingresada por el usuario, la idea es comparar los índices de la palabra. Para esto se define un inicio y un final para el recorrido por sus índices. El objetivo es comparar el primer índice con el último, el segundo con el penúltimo y así sucesivamente. En caso de que los ínidices sean diferentes la palabra no es palíndromo. Si la función tras hacer la comparación encuentra que no hay diferencia entre los índices comparados, entonces detecta que la palabra es un palíndromo

### Reto 1.3

Escribir una función que reciba una lista de números y devuelva solo aquellos que son primos. La función debe recibir una lista de enteros y retornar solo aquellos que sean primos.

```python
def detecta_primos(num):
  if num < 2: 
    return False
  for i in range(2, num):  
    if num % i == 0:  
      return False 
  return True

print("Ingrese por favor una lista de números (0 para terminar): ") 

numeros = []

while True: 
  numero_ingresado=int(input("Número: ")) 
  if numero_ingresado == 0: 
    break
  numeros.append(numero_ingresado) 

numeros.sort() 

def lista_de_primos(numeros):
  primos = [] 
  for num in numeros:
    if detecta_primos(num): 
      primos.append(num)  
      
  return primos
      
      
print("La lista de números del usuario es: ", numeros)

primos = lista_de_primos(numeros) 

print("De esa lista de  números, los primos son: ", primos)
```
Para saber si un número es primo o no, primero se deben descartar los números menores a 2, 1 o 0 no son primos. Luego se verifica si alguno de los numeros ingresados por el usuario es divisible por algún número entre 2 y los números ingresados. En caso de no serlo, entonces el número es primo. Con esto en mente, se ordena la lista ingresada por el usuario de menor a mayor, se llama a la función y los números que cumplan con el requisito son ingresados en una nueva lista que se muestra en consola.

### Reto 1.4
Escribir una función que reciba una lista de números enteros y retorne la mayor suma entre dos elementos consecutivos.

```python
print("Ingrese por favor una lista de números (digitar 0 para terminar): ") 

lista_de_numeros = [] 

while True: 
  numero_ingresado=int(input("Número: ")) 
  if numero_ingresado == 0: 
    break
  lista_de_numeros.append(numero_ingresado)  
  

def suma_mayor_consecutiva (lista_de_numeros):
    mayor = 0 
    
    for i in range(len(lista_de_numeros)-1):  
        suma = lista_de_numeros[i] + lista_de_numeros[i+1] 
        if suma > mayor: 
            mayor = suma
        
    return mayor

mayor = suma_mayor_consecutiva(lista_de_numeros)

print("La lista entregada por el usuario es: ", lista_de_numeros)

print("La suma de mayor valor es:", mayor)
```


La idea pensada para la función fue poder comparar cada par de números de la lista ingresada por el usuario a partir de sus índices. Se estableció un comparador "mayor" que se comparó con la suma de los números que eran consecutivos en la lista. En caso de que la suma fuese mayor al comparador, entonces este tomaba el valor de la suma y se iba actualizando por cada par de números hasta encontrar la suma de valor mayor

### Reto 1.5
Escribir una función que reciba una lista de string y retorne unicamente aquellos elementos que tengan los mismos caracteres. e.g. entrada: ["amor", "roma", "perro"], salida ["amor", "roma"]

```python
def encuentra_anagramas(lista_palabras):
    diccionario_anagramas = {} 
    for palabra in lista_palabras:   
        palabras_ordenadas = tuple(sorted(palabra)) 
        if palabras_ordenadas in diccionario_anagramas: 
            diccionario_anagramas[palabras_ordenadas].append(palabra) 
        else:
            diccionario_anagramas[palabras_ordenadas] = [palabra] 
   
    resultado = []    
    
    for grupo_palabras in diccionario_anagramas.values(): 
        if len(grupo_palabras) > 1: 
            for palabra in grupo_palabras: 
                resultado.append(palabra)
                
    return resultado
     

lista_palabras = input("Ingrese las palabras separadas por espacios: ").split()
print("Los anagramas de la lista ingresada son: ", encuentra_anagramas(lista_palabras))  
```

Para esta función inicialmente se pensó en comparar la longitud de las palabras con la cantidad de caracteres no repetidos de las mismas. Sin embargo, a pesar de ser exitoso para palabras con vocales repetidas, no funcionaba con palabras como "sol" o "paz". Por ende se pensó en otro método que consistió en usar un diccionario para almacenar las palabras. Cada palabra ingresada por el usuario se descompuso en sus letras individiduales y se ordenó alfabéticamente. Lo anterior se usó para nombrar a las claves del diccionario. La idea de la función fue lograr relacionar las palabras de la lista dada con claves dentro del diccionario, y en caso de encontrar coincidencias en letras, almacenar cada palabra como un valor en su respectiva clave. La idea fue que por cada clave existieran la mayor cantidad de palabras con los mismos caracteres de la clave y se guardaran en una lista. Posteriormente esta lista de values, sería impresa como una lista que contendría a las palabras que fuesen anagramas.
