"""Condicionales 1. Ejercicio: Dado un número, imprime si es positivo o negativo. 2. Ejercicio: Dado un número, imprime si es par o impar. 3. Ejercicio: Dado tres números, encuentra y muestra el mayor de ellos. 
"""

numero = 10
if numero < 0:
  print("numero es negativo")
if numero >=0:
  print("numero es positivo")

# otra forma

numero = -3
if numero < 0:
  print("numero es negativo")
else:
  print("numero es positivo")

numero = 5
if numero % 2 ==0:
  print("par")
else:
  print("impar")

a= 8
b = 10
c= 15

if a>b and a>c:
  print("el mayor es:",a)
elif b>c:
  print("el mayor es:",b)
else:
  print("el mayor es:",c)

#otra forma
a, b, c = 8, 10, 15 
mayor = max(a, b, c) 
print("el mayor es",mayor) 



















