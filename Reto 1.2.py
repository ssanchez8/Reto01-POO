#Realice una función que permita validar si una palabra es un 
#palíndromo. Condición: No se vale hacer slicing para invertir 
#la palabra y verificar que sea igual a la original.

palabra = input("Ingrese su palabra aquí: ")

def detecta_palindromo(palabra):
    palabra = palabra.lower()  #Se convierte la palabra a minúscula
    inicio = 0 #Se define un inicio y un final para recorrer la palabra por sus índices
    final = len(palabra)-1 #El índice final corresponde al tamaño de la palabra - 1 posición
    
    while inicio < final: #Se ejecuta el while recorriendo desde el índice 0 al final
        if palabra[inicio] != palabra[final]: #En caso de que los índices estudiados sean diferentes, no es palíndromo
            return False 
        inicio += 1 #Se comparan índices, si son iguales, se compara el segundo con el penúltimo. 
        final -= 1 #Se recorre la palabra completa, letra por letra, verificando si hay coincidencias
        
    return True #Si finalmente no se detectan letras diferentes entre índices, la función devuelve True

if detecta_palindromo(palabra):
    print("Es palíndromo")
else: 
    print("No es palíndromo") 