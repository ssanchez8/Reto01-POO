#Escribir una función que reciba una lista de números y 
#devuelva solo aquellos que son primos. La función debe 
#recibir una lista de enteros y retornar solo aquellos que sean primos.


def detecta_primos(num):
  if num < 2: #Si el número de la lista es menor a 2 no es primo. 1 no es primo.
    return False
  for i in range(2, num): #Verifico si el número de la lista es divisible por algún otro numero desde 2. En caso de serlo, no es primo. 
    if num % i == 0:  #Al tomar num = 2, se "cortocircuita" el for y la función retorna true, pues 2 es primo.
      return False 
  return True

print("Ingrese por favor una lista de números (0 para terminar): ") 

numeros = [] #Creo una lista vacía para guardar los números digitados por el usuario

while True: 
  numero_ingresado=int(input("Número: ")) #Se le pide al usuario una lista de números que quiere verificar
  if numero_ingresado == 0: #Si el número es 0 se rompe el ciclo para cerrar la lista de números
    break
  numeros.append(numero_ingresado) 

numeros.sort() #Ordeno la lista de números dada de menor a mayor.

def lista_de_primos(numeros):
  primos = [] #Creo una lista para almacenar los números que son primos
  for num in numeros:
    if detecta_primos(num): #Llamo la función que detecta si los números son primos, con num recorriendo la lista numeros
      primos.append(num)  #Finalmente, en caso de ser primos, los números entran en la lista creada al inicio de la función
      
  return primos
      
      
print("La lista de números del usuario es: ", numeros)

primos = lista_de_primos(numeros) #Se llama la función que contiene a la lista de primos

print("De esa lista de  números, los primos son: ", primos)
