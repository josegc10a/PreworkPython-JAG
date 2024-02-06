#Ejercicio 1: Conversor de Temperatura Escribe un programa que convierta una temperatura de grados Celsius a grados Fahrenheit. 
def celsius_a_fahrenheit(celsius):
    fahrenheit = ((celsius)*9/5 +32)
    return fahrenheit
temperatura_celsius = float(input("Ingresa la temperatura en grados Celsius: "))
temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)
print(f"{temperatura_celsius} grados Celsius son {temperatura_fahrenheit} grados Fahrenheit.")

#Ejercicio 2: Calculadora de Propina Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo una propina del 15% sobre el total de la cuenta. 
def total_restaurante (lista):
  suma=0
  for precio in lista:
    suma += precio
    suma_con_propina= suma*1.15
  return suma_con_propina
mi_lista = [50,20,30,40]
print(f"el total de la cuenta es:{total_restaurante(mi_lista)}€")
      

# Ejercicio 3: Verificación de Edad Escribe un programa que solicite la edad de un usuario y determine si es mayor de edad (mayor o igual a 18 años) o no. 
def es_mayor_edad (años):
    if años >=18: 
      return "Es mayor de edad"
    else:
      return "No es mayor de edad"
edad = int(input("Ingresa tu edad: "))  
mayor_de_edad=es_mayor_edad(edad)
print(mayor_de_edad)
 

# Ejercicio 4: Contador de Vocales Crea un programa que cuente el número de vocales en una palabra ingresada por el usuario.

def cuenta_vocales(string):
  vocales="aeiouAEIOU"
  contador=0
  for vocal in string:
    if vocal in vocales:
      contador +=1
  return contador
palabra = input("Ingresa una palabra: ")
cantidad_de_vocales = cuenta_vocales(palabra)
print (cantidad_de_vocales)

# Ejercicio 5: Suma de Números Pares Escribe un programa que calcule la suma de todos los números pares del 1 al 100. 

def suma_pares (n):
  suma=0
  for numero in range(1,n+1):
    if numero%2==0:
      suma +=numero
  return suma
print(suma_pares(100))
 
# Ejercicio 6: Verificación de Palíndromo Crea un programa que verifique si una palabra ingresada por el usuario es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda). 

def es_palindromo(palabra1):
  palabra1 = palabra1.lower()
  return palabra1 == palabra1[::-1]
palabra_introducida= input("Ingresa una palabra: ")
if es_palindromo(palabra_introducida):
  print("La palabra es un palíndromo.")
else:
  print("La palabra no es un palíndromo.")
  
# Ejercicio 7: Calculadora Simple Crea un programa que realice operaciones aritméticas simples (suma, resta, multiplicación, división) según la elección del usuario.

def calculadora():
  operacion = int(input("Elige operacion:[1,suma],[2,resta],[3,multiplicacion],[4,division]:  "))
  return operacion
opcion=calculadora()
if opcion==1: 
  num1=float(input("Introduce el primer numero: "))
  num2=float(input("Introduce el primer numero: "))
  resultado = num1+num2
  print(f"El resultado de la suma es: {resultado}")
elif opcion==2: 
  num1=float(input("Introduce el primer numero: "))
  num2=float(input("Introduce el primer numero: "))
  resultado = num1-num2
  print(f"El resultado de la resta es: {resultado}")
elif opcion == 3:
  num1 = float(input("Introduce el primer número: "))
  num2 = float(input("Introduce el segundo número: "))
  resultado = num1 * num2
  print(f"El resultado de la multiplicación es: {resultado}")
elif opcion == 4:
    num1 = float(input("Introduce el numerador: "))
    num2 = float(input("Introduce el denominador: "))
    if num2 != 0:
        resultado = num1 / num2
        print(f"El resultado de la división es: {resultado}")
    else:
        print("No se puede dividir entre cero.")
else:
    print("Opción no válida. Por favor, elige una operación válida.")

# Ejercicio 8: Cálculo del Índice de Masa Corporal (IMC) Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona. 

def calcula_IMC ():
  peso = float(input("Introduce tu peso en KG:  "))
  altura = float(input("Introduce tu altura en m:  "))
  IMC= peso/altura**2
  return IMC
resultado_IMC=calcula_IMC()
print(f"Tu indice de masa corporal es:{resultado_IMC}")

# Ejercicio 9: Conversor de DivisasEjercicios Introducción a Python: Enunciados 2 Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que 1 dólar es igual a 0.85 euros.
def conversor_divisa ():
  Dolares = float(input("Introduce el importe en $:  "))
  Euros = Dolares*0.85 
  return Euros
resultado_cambio=conversor_divisa()
print(f"Los dolares introducidos al cambio son:{resultado_cambio}€")

# Ejercicio 10: Determinar el Día de la Semana Escribe un programa que determine el día de la semana correspondiente a un número ingresado por el usuario (1 para lunes, 2 para martes, etc.). 
def dia_de_semana():
  dia = int(input("Introduce el numero del dia de la semana del 1 al 7: "))
  if 1<= dia <=7:
    return dia
  else:
    print("Introduce un numero del 1 al 7.")
    return None
numero_dia=dia_de_semana()
if numero_dia==1: 
  print ("el dia introducido es el Lunes")
elif numero_dia==2: 
  print ("el dia introducido es el Martes")
elif numero_dia==3: 
  print ("el dia introducido es el Miercoles")
elif numero_dia==4: 
  print ("el dia introducido es el Jueves")
elif numero_dia==5: 
  print ("el dia introducido es el Viernes")
elif numero_dia==6: 
  print ("el dia introducido es el Sabado")
elif numero_dia==7: 
  print ("el dia introducido es el Domingo")
else: 
  print ("haz caso")


#Ejercicio 11: Calculadora de Edad Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad actual. 

def calculo_edad():
    año_nacimiento = int(input("Introduce tu año de nacimiento: "))
    if año_nacimiento<=2024:
        diferencia = 2024 - año_nacimiento
        return diferencia
    else:  
        print ("no has nacido todavia")
        return None     
edad = calculo_edad()
if edad is not None:
    print(f"Tienes aproximadamente {edad} años.")
else:
    print("sigues sin nacer")


#Ejercicio 12: Calculadora de Área de un Rectángulo Crea un programa que calcule el área de un rectángulo. El usuario debe ingresar la longitud y el ancho del rectángulo.
def area_rectangulo():
  longitud=float(input("introduce la longitud en cm: "))
  ancho=float(input("introduce el ancho en cm: "))
  area=longitud*ancho
  return area
superficie =area_rectangulo()
print(f"El area del rectangulo es: {superficie}")

#Ejercicio 13: Verificación de Número Primo Escribe un programa que determine si un número ingresado por el usuario es primo o no. 
def es_primo(numero): 
    if numero <= 1: 
        return False
    for i in range(2, numero): 
        if numero % i == 0: 
            return False 
    return True 
num = int(input("Ingresa un número: ")) 
if es_primo(num): 
    print("Es un número primo.") 
else: 
    print("No es un número primo.")
 
#Ejercicio 14: Calculadora de Descuento Crea un programa que calcule el precio final de un artículo después de aplicar un descuento del 20%.
def calculadora_descuento ():
  precio =float(input("Introduce precio del articulo: "))
  precio_final= precio*0.8
  return precio_final
con_el_descuento= calculadora_descuento()
print(f"Aplicado el descuento el precio se queda en: {con_el_descuento}€")

# Ejercicio 15: Conversor de Tiempo Escribe un programa que convierta un número de minutos en horas y minutos. Por ejemplo, 145 minutos serían 2 horas y 25 minutos. 
def conversor_tiempo ():
  min= int(input("Introduce una cantidad de minutos: "))
  dividir_entre_60 = min/60
  horas= int(dividir_entre_60)
  parte_decimal = dividir_entre_60 % 1
  minutos =parte_decimal*60
  minutos_redondeo= round(minutos)
  print(f"Todos estos {min} corresponden a {horas} horas y {minutos_redondeo} minutos")
  return
conversor_tiempo()

# Ejercicio 16: Contador de Números Pares e Impares Crea un programa que cuente y muestre la cantidad de números pares e impares en una lista ingresada por el usuario.
def contador (lista):
    numeros_pares=0
    numeros_impares=0
    for i in lista:
      if i%2==0:
        numeros_pares +=1 
      else:
        numeros_impares +=1
    return numeros_pares, numeros_impares
numeros_str = input("Introduce una lista de números enteros separados por espacios: ")
lista_numeros = [int(numero) for numero in numeros_str.split()]
pares, impares = contador(lista_numeros)
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")

#Ejercicio 17: Conversor de Millas a Kilómetros Escribe un programa que convierta una distancia en millas a kilómetros. Sabiendo que 1 milla equivale a 1.60934 kilómetros. 

def conversor_milla_a_km ():
  Milla = float(input("Introduce la distancia en millas:  "))
  km = round(Milla/1.60934,2) 
  return km
resultado_cambio=conversor_milla_a_km()
print(f"Las millas introducidas equivalen a:{resultado_cambio}km")

# Ejercicio 18: Contador de PalabrasEjercicios Introducción a Python: Enunciados 3 Crea un programa que cuente la cantidad de palabras en una oración ingresada por el usuario. 
def contador_palabras (lista):
    n_palabras=len(lista)
    return n_palabras
palabras_str = input("Introduce una oracion: ")
cantidad_palabras = palabras_str.split()
palabras = contador_palabras(cantidad_palabras)
print(f"Cantidad de palabras: {palabras}")

#Ejercicio 19: Verificación de Año Bisiesto Escribe un programa que determine si un año ingresado por el usuario es bisiesto o no.

def año_bisiesto(numero): 
    if numero <= 1: 
        return False
    if numero % 4 == 0: 
      return True 
año = int(input("Ingresa un año: ")) 
es_año_bisiesto = año_bisiesto(año)
if es_año_bisiesto ==True:
  print(f"El año introducido {año} es año bisiesto")
else:
  print(f"El año introducido {año} NO es año bisiesto")

#Ejercicio 20: Suma de Números en una Lista Crea un programa que sume todos los números en una lista ingresada por el usuario.

def sumar (lista):
    suma=0
    for i in lista:
        suma +=i 
    return suma
numeros_str = input("Introduce una lista de números separados por espacios: ")
lista_numeros = [float(numero) for numero in numeros_str.split()]
suma_lista = sumar(lista_numeros)
print(f"La suma total de la lista es: {suma_lista}")
