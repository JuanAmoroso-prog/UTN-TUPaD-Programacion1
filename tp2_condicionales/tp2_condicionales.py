print("------------------------------------------------------------")

print("1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”. ")

edad=int(input("Ingresar edad de usuario: "))
if edad>18:
  print("Es mayor de edad.")

print("------------------------------------------------------------")

print("2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”. ")

nota=int(input("Ingrese nota del usuario: "))
if nota>=6:
  print("Aprobado.")
else:
  print("Desaprobado.")

print("------------------------------------------------------------")

print("3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje (Ha ingresado un número par); en caso contrario, imprimir por pantalla (Por favor, ingrese un número par). Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar. ")

n1=int(input("Ingresar un numero par: "))
if n1%2==0:
  print("Ha ingresado un numero par.")
else:
  print("Por favor, ingrese un número par. ")

print("------------------------------------------------------------")

print("4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:• Niño/a: menor de 12 años.• Adolescente: mayor o igual que 12 años y menor que 18 años.• Adulto/a joven: mayor o igual que 18 años y menor que 30 años.• Adulto/a: mayor o igual que 30 años. ")

edad=int(input("Ingrese edad de usuario: "))

if edad<12:
  print("Niño.")
elif edad>=12 and edad<18:
  print("Adolescente.")
elif edad>=18 and edad<30:
  print("Adulto/a joven")
elif edad>=30:
  print("Adulto.")

print("------------------------------------------------------------")

print("5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje (Ha ingresado una contraseña correcta); en caso contrario, imprimir por pantalla (Por favor, ingrese una contraseña de entre 8 y 14 caracteres).") 


contraseña=len(input("Introducir contraseña: "))
print(f"Contador de letras: {contraseña}.")
if contraseña>=8 and contraseña<=14:
  print("Ha introducido una contraseña correcta.")
else:
  print("Por favor, introduce una contraseña entre 8 y 12 caracteres.")

print("------------------------------------------------------------")

print("6) Escribir un programa que solicite al usuario el consumo mensual de energía eléctrica enkilovatios (kWh) e indique la categoría del consumo según el siguiente criterio:• Menor que 150 kWh: “Consumo bajo”.• Entre 150 y 300 kWh (inclusive): “Consumo medio”.• Mayor que 300 kWh: “Consumo alto”.Además, si el consumo supera los 500 kWh, mostrar un mensaje adicional que diga:“Considere medidas de ahorro energético”.El programa debe imprimir por pantalla la categoría correspondiente.")

kwh=int(input("Introducir consumo energético en Kwh: "))

if kwh<150:
  print("Consumo bajo.")
elif kwh>=150 and kwh<=300:
  print("Consumo medio")
elif kwh>300 and kwh<=500:
  print("Consumo alto.")
else:
  print("Consumo alto.")
  print("Considere medidas de ahorro energético.")

print("------------------------------------------------------------")

print("7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.")

palabra=input("Ingresar una palabra: ")
if palabra.lower().endswith(("a","e","i","o","u")):
  print(f"{palabra}!")
else:
  print(palabra)

print("------------------------------------------------------------")

print("8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee: 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. El programa debe transformar el nombre ingresado de acuerdo con la opción seleccionada por el usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.")

nombre=input("Ingresá tu nombre: ")
print("Ingresá un número del 1 al 3 siendo: ")
print("1-Para que tu nombre esté en mayúsculas.")
print("2-Para que tu nombre aparezca en minúsculas. ")
print("3-Para que la primer letra del nombre aparezca en mayúscula.")
n=int(input())

if n==1:
  nombre=nombre.upper()
  print(nombre)
elif n==2:
  nombre=nombre.lower()
  print(nombre)
elif n==3:
  nombre=nombre.title()
  print(nombre)

print("------------------------------------------------------------")

print("9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla: • Menor que 3: Muy leve (imperceptible). • Mayor o igual que 3 y menor que 4: Leve (ligeramente perceptible). • Mayor o igual que 4 y menor que 5: Moderado (sentido por personas, pero generalmente no causa daños). • Mayor o igual que 5 y menor que 6: Fuerte (puede causar daños en estructuras débiles). • Mayor o igual que 6 y menor que 7: Muy Fuerte (puede causar daños significativos). • Mayor o igual que 7: Extremo (puede causar graves daños a gran escala). ")

magnitud=int(input("Introducir magnitud de terremoto: "))

if magnitud<3:
  print("Muy leve (imperceptible).")
elif magnitud==3:
  print("Leve (ligeramente perceptible).")
elif magnitud==4:
  print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif magnitud==5:
  print("Fuerte (puede causar daños en estructuras débiles).")
elif magnitud==6:
  print("Muy fuerte (puede causar daños significativos).")
elif magnitud>=7:
  print("Extremo (puede causar graves daños a gran escala).")

print("------------------------------------------------------------")

print("10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año : Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.")

#uso un len() para guardar el valor numerico del largo de la palabra.
hemisferio=len(input("¿En qué hemisferio te encontrás (norte o sur)?: "))
mes=int(input("¿Qué mes del año es (1-12)?: "))
dia=int(input("¿Qué fecha del mes es? "))


if hemisferio==5:
  
  if (mes==12 and dia>=21) or ((mes>=1 and mes<4) and dia<=20):
      print("Te encontrás en el hemisferio norte, en invierno.")

  elif (mes==3 and dia>=21) or (mes<=6 and dia<20):
      print("Te encontras en el hemisferio norte, en primavera")

  elif (mes==6 and dia>=21) or (mes<=9 and dia<20):
      print("Te encontras en el hemisferio norte, en verano")

  elif (mes==9 and dia>=21) or (mes<=12 and dia<20):
      print("Te encontras en el hemisferio norte, en otoño")

elif hemisferio==3:
    
  if (mes==12 and dia>=21) or ((mes>=1 and mes<4) and dia<=20):
      print("Te encontrás en el hemisferio sur, en verano.")

  elif (mes==3 and dia>=21) or (mes<=6 and dia<20):
      print("Te encontras en el hemisferio sur, en otoño.")

  elif (mes==6 and dia>=21) or (mes<=9 and dia<20):
      print("Te encontras en el hemisferio sur, en invierno.")

  elif (mes==9 and dia>=21) or (mes<=12 and dia<20):
      print("Te encontras en el hemisferio sur, en primavera.")

