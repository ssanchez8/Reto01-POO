#Crear una función que realice operaciones 
#básicas (suma, resta, multiplicación, división) entre dos números, según la elección del usuario, la forma de entrada 
#de la función será los dos operandos y el caracter usado para la operación. entrada: (1,2,"+"), salida (3).

numero1 = float(input("Por favor ingresa el primer número a operar: "))
operacion = input("Por favor selecciona la operación (+, -, *, /): ")
numero2 = float(input("Por favor ingresa el segundo número a operar: ")) #Se piden los números y la operación


def calculos(numero1, numero2, operacion):
    if operacion == "+": #Se compara la operación digitada, y se ejecuta la respectiva operación entre los números
        return numero1 + numero2
    elif operacion == "-":
        return numero1 - numero2
    elif operacion == "*":
        return numero1 * numero2
    elif operacion == "/":
        if numero2 !=0: #En caso de dividir por cero se aclara que la división no es posible
            return numero1 / numero2
        else:
            print("La división por cero no es posible")
    else: 
        print("La operación no es válida") #En caso de que el usuario meta otros valores, la operación será inválida
        
    
resultado = calculos(numero1, numero2, operacion) #Se llama a la función con los parámetros

if resultado is not None: #Se imprime la operación deseada en caso de que resultado no sea nulo
  print(f"El resultado de {numero1} {operacion} {numero2} es {resultado}") 