
print("------------------------------------------------------------------")
#Actividad 1

print("1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.")


print(" Hola Mundo")

print("------------------------------------------------------------------")
#Actividad 2

print("2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.")

nombre=input("Ingresa un nombre: ")
print(f"Hola {nombre}!")

print("------------------------------------------------------------------")
#Actividad 3

print("3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.")

nombre=input("Ingresá un Nombre:")
apellido=input("Ingresá un Apellido:")
edad=input("Ingresá una edad:")
residencia=input("Ingresá un lugar de residencia:")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")


print("------------------------------------------------------------------")
#Actividad 4

print("4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.")

radio=float(input("Introducir radio de un circulo: "))
area=3.1416*radio**2
perimetro=2*3.1416*radio
print(f"El area del circulo es {area}, y su perímetro es de {perimetro}.")


print("------------------------------------------------------------------")
#Actividad 5

print("5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.")

segundos=int(input("Ingrese una cantidad de segundos:"))
horas=segundos/3600
horas=int(horas)
print(f"La cantidad de horas a la que equivalen esos segundos es de {horas} hora/s.")

print("------------------------------------------------------------------")
#Actividad 6

print("6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.")

numero1=int(input("Introducir un numero: "))
numero=numero1*1
print(numero)
numero=numero1
numero=numero1*2
print(numero)
numero=numero1*3
print(numero)
numero=numero1*4
print(numero)
numero=numero1*5
print(numero)
numero=numero1*6
print(numero)
numero=numero1*7
print(numero)
numero=numero1*8
print(numero)
numero=numero1*9
print(numero)
numero=numero1*10
print(numero)


print("------------------------------------------------------------------")
#Actividad 7

print("7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.")

n1=int(input("Ingresar el primer numero: "))
n2=int(input("Ingresar el segundo numero: "))

suma=n1+n2
resta=n1-n2
restaalreves=n2-n1
multiplicacion=n1*n2
division=n1/n2
divisionalreves=n2/n1
print(f"El resultado de sumarlos es: {suma}.")
print(f"El resultado de restar el primer numero con el segundo es: {resta}.")
print(f"El resultado de restar el segundo numero con el primero es: {restaalreves}.")
print(f"El resultado de multiplicarlos es: {multiplicacion}.")
print(f"El resultado de dividir el primer numero por el segundo es: {division}.")
print(f"El resultado de dividir el segundo numero por el primero es: {divisionalreves}.")

print("------------------------------------------------------------------")
#Actividad 8

print("8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo: 𝐼𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔 (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)2")

altura=float(input("ingresar altura: "))
peso=float(input("Ingrear peso en KG: "))
imc=peso/altura**2

print(f"El indice de masa corporal es de {imc}.")

print("------------------------------------------------------------------")
#Actividad 9

print("9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia: 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9 5 . 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32 ")

grados=float(input("Ingresar temperatura en grados Celcius: "))
fahr=9/5*grados+32

print(f"El equivalente de esos grados celcius en fahrenheit es de: {fahr}.")

print("------------------------------------------------------------------")
#Actividad 10

print("10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números. ")

n1=int(input("Ingresar el primer numero: "))
n2=int(input("Ingresar el segundo numero: "))
n3=int(input("Ingresar el tercer numero: "))

promedio=(n1+n2+n3)/3

print(f"El promedio de esos 3 numeros es {promedio}.")

