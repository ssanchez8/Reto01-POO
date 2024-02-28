#Escribir una función que reciba una lista de 
# números enteros y retorne la mayor suma entre dos elementos consecutivos.

print("Ingrese por favor una lista de números (digitar 0 para terminar): ") 

lista_de_numeros = [] #Se crea una lista vacía para guardar los números digitados por el usuario

while True: 
  numero_ingresado=int(input("Número: ")) #Se le pide al usuario una lista de números que quiere verificar
  if numero_ingresado == 0: #Si el número es 0 se rompe el ciclo para cerrar la lista de números
    break
  lista_de_numeros.append(numero_ingresado)  
  

def suma_mayor_consecutiva (lista_de_numeros):
    mayor = 0 #Se define un comparador que se detendrá en la suma de mayor valor
    
    for i in range(len(lista_de_numeros)-1): #Recorro los índices de la lista de números 
        suma = lista_de_numeros[i] + lista_de_numeros[i+1] #Se suman los números consecutivos
        if suma > mayor: #Si la suma es mayor al comparador, este toma el valor de la suma
            mayor = suma #Esto hace que la suma se actualice a la mayor en cada iteración
        
    return mayor

mayor = suma_mayor_consecutiva(lista_de_numeros)

print("La lista entregada por el usuario es: ", lista_de_numeros)

print("La suma de mayor valor es:", mayor)














