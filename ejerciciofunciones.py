"""Funciones 1. Ejercicio: Define una función que tome dos números y retorne su suma. """
def suma():
  a= 5
  b= 2
  suma = a +b
  print(suma)

suma()



def suma(a,b):
  return a+b
print (suma(5,3))

# 2. Ejercicio: Defineuna función que tome un número y retorne su factorial.

def calabaza (a):
  if a==0:
    return 1
  else:
    return a*calabaza(a-1)
print(calabaza(5))

"""3. Ejercicio: Define una función que tome un número y determine si es primo.
numero primo su division es solo por el 1 y el mismo"""

def es_primo(num):
  if num < 2:
      return False
  for i in range(2,num):
      if (num % i) ==0:
        return False
  return True
 
print(es_primo(100))


"""4. Ejercicio: Define una función que reciba una lista de números y retorne la suma
de ellos."""

def suma_lista(list):
   return sum(list)
print (suma_lista([1,2,3,4,5]))

"""5. Ejercicio: Define una función que reciba una cadena de texto y retorne la
cadena en reversa."""

def reversa(cadena):
   return cadena [::-1]
print (reversa ("hola"))





  





