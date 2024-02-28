#Escribir una función que reciba una lista de string y retorne unicamente aquellos 
# elementos que tengan los mismos caracteres. e.g. entrada: 
# ["amor", "roma", "perro"], salida ["amor", "roma"]

def encuentra_anagramas(lista_palabras):
    diccionario_anagramas = {} #Se crea un diccionario vacío, la idea será almacenar palabras por claves dependiendo de sus letras
    for palabra in lista_palabras:   #Se recorre la lista dada por el usuario, de cada palabra se toman sus caracteres y se ordenan
        palabras_ordenadas = tuple(sorted(palabra)) #Se convierte la palabra ordenada en una tupla
        if palabras_ordenadas in diccionario_anagramas: #Se verifica si la clave está en el diccionario, si sí, se agrega la palabra como value
            diccionario_anagramas[palabras_ordenadas].append(palabra) 
        else:
            diccionario_anagramas[palabras_ordenadas] = [palabra] #Si no, se crea un key con la tupla de letras y se agrega la palabra como value
   
   
    resultado = []    
    
    for grupo_palabras in diccionario_anagramas.values(): #Se recorre el diccionario y se toman los values
        if len(grupo_palabras) > 1: #Los values con una sola palabra se descartan
            for palabra in grupo_palabras: #Se recorre cada palabra en el value y se agrega al resultado
                resultado.append(palabra)
                
    return resultado
     

lista_palabras = input("Ingrese las palabras separadas por espacios: ").split()
print("Los anagramas de la lista ingresada son: ", encuentra_anagramas(lista_palabras))  # Output: List of anagrams

