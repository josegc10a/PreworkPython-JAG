"""Ejercicios nivel básico"""
"""1. Crea una función para verificar si un número es par o impar y devuelva “El
número es par” o “El número es impar” según corresponda."""
def es_par_o_impar(numero):
  return numero%2==0 
num=int(input("ingresa un numero:"))
if es_par_o_impar(num):
   print("es un numero par.")
else: 
   print ("es un numero impar.")

"""Crea una función a la que pases un número como argumento, calcule el factorial de
ese número y haga print del resultado."""
   
def factorial(numero):
  resultado=1
  for i in range(1,numero+1):
    resultado*=i 
  return resultado 
  num = int(input("Ingresa un numero:"))
print("El factorial de", num,"es:",factorial(num))

"""Crea una función a la que se le pase un número como argumento, calcule la
cantidad de dígitos y haga print de “La cantidad de dígitos es:” y el resultado
total de dígitos.
PISTA: Para convertir un número a string usa el método str(). Te recordamos que
para saber la longitud de una cadena utilizamos len()"""

def contar_digitos(numero):
  return len(str(numero)) 
num = int(input("Ingresa un número: ")) 
print("La cantidad de dígitos es:", contar_digitos(num))

"""1. Dada una lista de números, crea una función que devuelva el número máximo
de la lista."""

def encontrar_maximo(lista):
  maximo=lista[0]
  for numero in lista:
    if numero>maximo:
      maximo=numero
  return maximo 
mi_lista = [1,2,3,4,5]
print(encontrar_maximo(mi_lista))

def encontrar_maximo(lista): 
  maximo = lista[0] 
  for numero in lista: 
    if numero > maximo: 
      maximo = numero 
  return maximo 
numeros = [5, 12, 3, 8, 9]
print("El número máximo es:", encontrar_maximo(numeros))

"""Crea una función que, dado un número, sume los dígitos de ese número y
devuelva el resultado."""
def sumar_digitos(numero):
  suma = 0
  while numero > 0: 
    suma += numero % 10 
    numero //= 10
  return suma 
num = int(input("Ingresa un número: "))
print("La suma de los dígitos es:", sumar_digitos(num))

"""Dados dos números, crea una función para encontrar el mínimo común múltiplo
(MCM) de los dos números, que se les pasarán como argumento a la función, y
devuelva el MCM."""

def mcm(a, b): 
  if a == 0 or b == 0:
     return 0 
  else:
    maximo = max(a, b) 
    while True:
      if maximo % a == 0 and maximo % b == 0:
        return maximo
      maximo += 1 
num1 = int(input("Ingrese el primer número: ")) 
num2 = int(input("Ingrese el segundo número: ")) 
print("El MCM es:", mcm(num1, num2))

"""Crea una función a la que, pasándole la base y la altura, calcule y devuelva el
área de un triángulo."""

def calcular_area_triangulo(base, altura):
   return (base * altura) / 2
base = float(input("Ingrese la base del triángulo: ")) 
altura = float(input("Ingrese la altura del triángulo: ")) 
print("El área del triángulo es:", calcular_area_triangulo(base, altura))

"""Crea una función que, dado un número, verifique si un número es positivo,
negativo o cero."""

def positivo_o_negativo(numero):
    if numero ==0:
       return"0"
    if numero <= 0:
      return "negativo"
    else:
       return "positivo"
numero = float(input("Ingresa un número: ")) 
print("El número es:",positivo_o_negativo (numero)) 

"""Crea una función que, dada una palabra, cuente la cantidad de letras en una
palabra."""
def contar_letras(palabra): 
  contador = 0 
  for letra in palabra: 
    if letra.isalpha(): 
      contador += 1 
  return contador 
palabra = input("Ingresa una palabra: ") 
print("La cantidadde letras es:", contar_letras(palabra))

"""Crea una función que, dada una palabra, cuente la cantidad de letras en una
palabra."""

def contar_letras(palabra): 
  contador = 0 
  for letra in palabra: 
       contador += 1 
  return contador 
palabra = input("Ingresa una palabra: ") 
print("La cantidadde letras es:", contar_letras(palabra))

"""Crea una función que, dada una lista de números, convierta la lista de números
a su valor absoluto."""

def valor_absoluto(lista):
  for i in range(len(lista)):
    lista[i] = abs(lista[i])  
  return lista 
numeros = [5, -12, 3, -8, 9] 
print("Lista con valores absolutos:", valor_absoluto(numeros))

"""Crea una función que, dado un número, verifique si un número es primo."""
 
def es_primo(numero):  
  if numero <= 1:
     return False
  if numero ==2:
     return True 
  for i in range(2, numero): 
     if numero % i == 0: 
      return False 
     return True 
num = int(input("Ingresa un número: ")) 
if es_primo(num): print("Es un número primo.") 
else: print("No es un número primo.")
   
"""Dados dos números, crea una función para encontrar el máximo común divisor
(MCD) de esos dos números."""

def mcd(a, b):
  while b:
     a, b = b, a % b 
  return a 

num1 = int(input("Ingresa el primer número: ")) 
num2 = int(input("Ingresa el segundo número: ")) 
print("El MCD es:", mcd(num1, num2))








