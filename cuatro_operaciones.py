#Agregando la primera operacion
def suma(a,b):
    return a+b

#funcion imprimir resultado
def imprimir_resultado(resultado):
    print("El resultado es: ", resultado)
    
# Description: Este archivo contiene las funciones que realizan las operaciones matematicas basicas
#Agregar input para que el usuario pueda ingresar los valores
a = int(input("Ingrese el primer valor: "))
b = int(input("Ingrese el segundo valor: "))

imprimir_resultado(suma(a,b))


