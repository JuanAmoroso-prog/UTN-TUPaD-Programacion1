#Ejercicio 1--"Caja del Kiosco"
#Objetivo: Simular una compra con validaciones y cálculo de total.

nombrecliente = input("Introducir nombre del cliente: ")  

#Validacion para que el nombre no contenga números ni espacios vacios. 
       
while not nombrecliente.isalpha() or nombrecliente=="":      
  print("Error, el nombre no debe contener números o espacios vacíos.")
  nombrecliente=input("Introducir nombre válido del cliente: ")

numprod = input("Introducir cantidad de productos a comprar: ")

#validacion para que la cantidad de productos sea un numero positivo.

while not numprod.isdigit() or int(numprod) <= 0:
  print("Error, la cantidad de productos debe estar representada por un número positivo.")
  numprod = input("Introducir un número válido a cantidad de productos a comprar: ")

print("--------------------------------------")

#inicializo variables para el calculo de totales y ahorros.
numprod=int(numprod)
ahorrotot = 0
total_con_desc = 0
total_sin_desc = 0

#itero para cada producto, solicitando su precio y si tiene descuento, con validaciones para ambos casos. Luego calculo el total con y sin descuento, y el ahorro total. Finalmente imprimo un resumen de la compra.
for i in range (1,numprod+1):

  precio = input(f"Introducir precio del producto {i}: $")
  while not precio.isdigit():
    print("Error, introducir valor numérico al precio.")
    precio = input(f"Introducir precio del producto {i}: $")

  precio = int(precio)
  total_sin_desc += precio

  tienedesc = input("Tiene descuento (S/N)?").lower()
  while tienedesc not in ["s", "n"]:
    tienedesc = input("Error, ingrese S o N: ").lower()

  if tienedesc == "s":
    diezporc = precio * 0.10
    precio_final = precio - diezporc
    ahorrotot += diezporc
  else: 
      precio_final = precio
  total_con_desc += precio_final

  print(f"Producto {i} - Precio: ${precio} Descuento (S/N): {tienedesc}.") 
  
#Imprimo el resumen de la compra, mostrando nombre del cliente, cant. de productos comprados, total sin descuentos, total con descuentos, ahorro total y promedio por producto.
print("--------------------------------------")  
promedio = total_con_desc/numprod  

print(f"Cliente:{nombrecliente}")
print(f"Cantidad de productos: {numprod}")

print("--------------------------------------") 
print(f"Total sin descuentos: ${total_sin_desc}")
print(f"Total con descuentos: ${total_con_desc:.2f}")
print(f"Ahorro: ${ahorrotot:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")

print("-------------------------------------------------------------------------")

#Ejercicio 2 — “Acceso al Campus y Menú Seguro”
#Objetivo: Login con intentos + menú de acciones con validación estricta.

#1. Definir credenciales fijas en el código:
#o usuario correcto: "alumno"
#o clave correcta: "python123"

usuario_correcto = "alumno"
clave_correcta = "python123"

#2. Permitir máximo 3 intentos para ingresar usuario y clave.
#3. Si falla 3 veces: mostrar “Cuenta bloqueada” y terminar.

intentos=0

while intentos<3:
  usuario = input("Ingrese su usuario:")
  clave = input("Ingrese su clave:")
  if usuario == usuario_correcto and clave == clave_correcta:

    #4. Si ingresa bien: mostrar un menú repetitivo (usar while) hasta elegir salir:
    #1. Ver estado de inscripción (mostrar “Inscripto”)
    #2. Cambiar clave (pedir nueva clave y confirmación; deben coincidir)
    #3. Mostrar mensaje motivacional (1 frase)
    #4. Salir
    #5. Validación del menú:
    # Debe ser número (.isdigit())
    # Debe estar entre 1 y 4

    while True:

      print("\nMenú de opciones:")
      print("1. Ver estado de inscripcion")
      print("2. Cambiar clave")
      print("3. Mostrar mensaje motivacional")
      print("4. Salir")

      opcion=input("Seleccione una opción del 1 al 4: ")
      while not opcion.isdigit():
        print("Error: ingrese un número válido.")
        opcion=input("Opción: ")
      while int(opcion) < 1 or int(opcion) > 4:
        print("Error: opción fuera de rango.")
        opcion=input("opcion: ")

      match opcion:
         
        case "1":
          print("--------------------------------------------------")
          print("Estado de inscripcion: Inscripto")
          
          #Cambio de clave
          #La nueva clave debe tener mínimo 6 caracteres (validar con len()), si no, rechazar.

        case "2":

          nueva_clave=input("Ingrese la nueva clave (mínimo 6 caracteres): ")

          while len(nueva_clave) < 6:
            print("Error, la clave debe tener al menos 6 caracteres.")
            nueva_clave=input("Ingrese una nueva clave válida (mínimo 6 caracteres): ")
          confirmacion_clave=input("Confirme la nueva clave: ")

          while confirmacion_clave != nueva_clave:
              print("Error, las claves no coinciden.")
              confirmacion_clave = input("Confirme la nueva clave: ")
          clave_correcta = nueva_clave
          print("Clave cambiada con éxito.")
        case "3":
          print("Te prometiste no rendirte y llegar hasta el final. Por un futuro del que esté orgulloso!")

        case "4":
          
          break
    break
  
  else:
    intentos += 1
    print(f"credenciales incorrectas. Intento {intentos} de 3.")
if intentos==3:
  print("Cuenta bloqueada.")


print("-------------------------------------------------------------------------")

# Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)”



opcion = "0"

paciente1 = ""
paciente2 = ""
paciente3 = ""
paciente4 = ""

paciente1_martes = ""
paciente2_martes = ""
paciente3_martes = ""

# Nombre operador
nombre_operador = input("Introducir nombre del operador: ")
while not nombre_operador.isalpha() or nombre_operador == "":
    print("Error, solo letras.")
    nombre_operador = input("Introducir nombre válido: ")

print(f"\nBienvenido {nombre_operador}")

while opcion != "5":
    print("\n1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Salir")

    opcion = input("Seleccionar opción: ")
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 5:
        opcion = input("Error. Seleccione opción válida: ")

    # ---------------- RESERVAR ----------------
    if opcion == "1":
        dia = input("Elegir día (1=Lunes, 2=Martes): ")
        while dia != "1" and dia != "2":
            dia = input("Error. Elegir 1 o 2: ")

        paciente = input("Nombre del paciente: ")
        while not paciente.isalpha() or paciente == "":
            paciente = input("Error. Solo letras: ")

        if dia == "1":
            # verificar repetido
            if paciente == paciente1 or paciente == paciente2 or paciente == paciente3 or paciente == paciente4:
                print("Paciente ya tiene turno el lunes")
            else:
                if paciente1 == "":
                    paciente1 = paciente
                elif paciente2 == "":
                    paciente2 = paciente
                elif paciente3 == "":
                    paciente3 = paciente
                elif paciente4 == "":
                    paciente4 = paciente
                else:
                    print("No hay turnos disponibles el lunes")

        else:
            if paciente == paciente1_martes or paciente == paciente2_martes or paciente == paciente3_martes:
                print("Paciente ya tiene turno el martes")
            else:
                if paciente1_martes == "":
                    paciente1_martes = paciente
                elif paciente2_martes == "":
                    paciente2_martes = paciente
                elif paciente3_martes == "":
                    paciente3_martes = paciente
                else:
                    print("No hay turnos disponibles el martes")

    # ---------------- CANCELAR ----------------
    elif opcion == "2":
        dia = input("Elegir día (1=Lunes, 2=Martes): ")
        while dia != "1" and dia != "2":
            dia = input("Error. Elegir 1 o 2: ")

        paciente = input("Nombre del paciente a cancelar: ")
        while not paciente.isalpha() or paciente == "":
            paciente = input("Error. Solo letras: ")

        if dia == "1":
            if paciente == paciente1:
                paciente1 = ""
                print("Turno cancelado correctamente")
            elif paciente == paciente2:
                paciente2 = ""
                print("Turno cancelado correctamente")
            elif paciente == paciente3:
                paciente3 = ""
                print("Turno cancelado correctamente")
            elif paciente == paciente4:
                paciente4 = ""
                print("Turno cancelado correctamente")
            else:
                print("Paciente no encontrado")

        else:
            if paciente == paciente1_martes:
                paciente1_martes = ""
                print("Turno cancelado correctamente")
            elif paciente == paciente2_martes:
                paciente2_martes = ""
                print("Turno cancelado correctamente")
            elif paciente == paciente3_martes:
                paciente3_martes = ""
                print("Turno cancelado correctamente")
            else:
                print("Paciente no encontrado")

    # ---------------- VER AGENDA ----------------
    elif opcion == "3":
        dia = input("Elegir día (1=Lunes, 2=Martes): ")
        while dia != "1" and dia != "2":
            dia = input("Error. Elegir 1 o 2: ")

        if dia == "1":
            print("\nAgenda Lunes:")
            print("Turno 1:", paciente1 if paciente1 != "" else "(libre)")
            print("Turno 2:", paciente2 if paciente2 != "" else "(libre)")
            print("Turno 3:", paciente3 if paciente3 != "" else "(libre)")
            print("Turno 4:", paciente4 if paciente4 != "" else "(libre)")
        else:
            print("\nAgenda Martes:")
            print("Turno 1:", paciente1_martes if paciente1_martes != "" else "(libre)")
            print("Turno 2:", paciente2_martes if paciente2_martes != "" else "(libre)")
            print("Turno 3:", paciente3_martes if paciente3_martes != "" else "(libre)")

    # ---------------- RESUMEN ----------------
    elif opcion == "4":
        ocupados_lunes = 0
        ocupados_martes = 0

        if paciente1 != "": ocupados_lunes += 1
        if paciente2 != "": ocupados_lunes += 1
        if paciente3 != "": ocupados_lunes += 1
        if paciente4 != "": ocupados_lunes += 1

        if paciente1_martes != "": ocupados_martes += 1
        if paciente2_martes != "": ocupados_martes += 1
        if paciente3_martes != "": ocupados_martes += 1

        print("\nResumen:")
        print("Lunes:", ocupados_lunes, "ocupados -", 4 - ocupados_lunes, "libres")
        print("Martes:", ocupados_martes, "ocupados -", 3 - ocupados_martes, "libres")

        if ocupados_lunes > ocupados_martes:
            print("Lunes tiene más turnos")
        elif ocupados_martes > ocupados_lunes:
            print("Martes tiene más turnos")
        else:
            print("Empate")

print("Sistema cerrado")

print("-------------------------------------------------------------------------")

#Ejercicio 4 — “Escape Room: La Bóveda”

#Variables fijas(NO SE PIDEN POR TECLADO):

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

#variables que encesité ingresar:
forzar_seguidas = 0


#Pedir nombre del agente y validar con .isalpha() en un while.
nombre_del_agente = input("Introducir nombre del agente: ")
while not nombre_del_agente.isalpha():
  print("Error, el nombre del agente debe estar conformado por letras.")
  nombre_del_agente=input("Introducir otro nombre para el agente: ")

  
#------------CONDICIONES DE FIN-------------

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 :

# Validar opciones del menú y cualquier número pedido con .isdigit() en un while.
  print("Estado:")
  print(f"La energía actual es: {energia}")
  print(f"El tiempo restante es: {tiempo}")
  print(f"La cantidad de cerraduras abiertas es de: {cerraduras_abiertas}")
  print(f"La alarma está: {alarma}")
  

  print("\n Elegir una opcion del 1 al 3: ")

  print("\n1-Forzar cerradura  (costo: -20 energía, -2 tiempo)")
  print("2-Hackear panel  (costo: -10 energía, -3 tiempo)")
  print("3-Descansar (costo: +15 energía (máx 100), -1 tiempo; si alarma ON: -10 energía extra)")

  opcion=input("tu opcion elegida será la: ")

  while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
    print("Error, solo podes elegir una opcion del 1 al 3.")
    opcion = input("\ntu opcion elegida será la: ")

  match opcion:
     
    case "1":

      energia -= 20
      tiempo -=2

      #----------Regla anti SPAM--------------

      forzar_seguidas += 1

      if forzar_seguidas == 3:
        print("La cerradura se trabó. Alarma activada")
        alarma = True

      else:
        if energia < 40:
          print("Riesgo de alarma")
        
          numero=input("ingresá un número del 1 al 3: ")

          while not numero.isdigit() or int(numero) < 1 or int(numero) > 3 :
            numero = input("número inválido. Introducí un numero del 1 al 3")
          
          if numero == "3" :
            alarma = True

            print("Alarma activada!")

          else:
            if not alarma:

              cerraduras_abiertas += 1

        else:
          if not alarma:

            cerraduras_abiertas += 1

    #hackear panel
    case "2":

      forzar_seguidas = 0
      energia -= 10
      tiempo -= 3

    #debe usar un for de 4 pasos mostrando progreso.
      for i in range (0,4):

        codigo_parcial += "A"
        print( "Paso", i + 1 )

      if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3 :
          
          print("¡Código completo! Se abrió una cerradura.")
          cerraduras_abiertas += 1
          codigo_parcial = ""
      

    case "3":

      tiempo -= 1
      forzar_seguidas = 0
      energia += 15

      if alarma == True:
          
          energia-=10

      if energia > 100:

        energia = 100
      

  if cerraduras_abiertas == 3 :
    print("VICTORIA!")
    break
  elif energia <= 0 or tiempo <=0 :
    print("DERROTA!")
    break
#------------REGLA DE BLOQUEO POR ALARMA-------------

  if alarma== True and tiempo <= 3 and cerraduras_abiertas < 3:

    print("Sistema bloqueado.")

    print("DERROTA! (bloqueo por alarma)")
    break    


print("-----------------------------------------------------")

#Ejercicio 5 — “Escape Room:"La Arena del Gladiador

#Variables predefinidas:

vida_del_gladiador = int (100)
vida_del_enemigo = int (100)
pociones_de_vida = int (3)
daño_base_ataque_pesado = int (15)
daño_base_del_enemigo = int (12)
turno_gladiador = True 

#Variables creadas:


critico = float()


print("\nEjercicio 5 — Escape Room: La Arena del Gladiador")

print("\n--------------------------BIENVENIDO A LA ARENA--------------------------------------")

nombre_del_gladiador=input("\nIngrese el nombre del Gladiador: ")
while not nombre_del_gladiador .isalpha() or nombre_del_gladiador == "":
   print("\nError, solo se permiten letras.")
   nombre_del_gladiador=input("\nIngrese un nombre válido para el Gladiador: ")
      
#El juego entra en un ciclo que se repite mientras ambos combatientes tengan más de 0 puntos de vida.
print("\n-------------------------INICIO DEL COMBATE-------------------------------")

while vida_del_enemigo > 0 and vida_del_gladiador > 0 :
   
    
     
    print(f"{nombre_del_gladiador} (HP: {vida_del_gladiador}) vs Enemigo (HP: {vida_del_enemigo}) | Pociones: {pociones_de_vida}")

    #Turno del gladiador:

    print("\nElegir acción: ")

    print("\n1-Ataque Pesado.")
    print("2-Rafaga Veloz.")
    print("3-Curar.")

    #valido para ver si el num. ingresado es 1, 2 o 3.

    opcion=input("\nIngresar un número del 1 al 3 : ")   
    while not opcion.isdigit() or int (opcion) < 1 or int (opcion) > 3:
        opcion=input("\nError, ingresar un número del 1 al 3 :")

    print("----------------------------------------------------------------")
    
    #inicio match para desarrollar opciones.

    match opcion :
        
          case  "1" :

            print("Ataque Pesado!.")
          
            #Si la vida del enemigo es menor a 20 puntos, el jugador realiza un "Golpe Crítico" multiplicando su daño base por 1.5 (resultado float)

            if vida_del_enemigo < 20:
             

              critico = daño_base_ataque_pesado * 1.5
            

              #Resta el daño a la vida del enemigo.

              vida_del_enemigo -= critico

              #Muestra un mensaje: "¡Atacaste al enemigo por X puntos de daño!"

              print(f"\nAtacaste al enemigo por {critico} puntos de daño.")

            else:
             
              #Resta el daño a la vida del enemigo.

              vida_del_enemigo -= daño_base_ataque_pesado

              #Muestra un mensaje: "¡Atacaste al enemigo por X puntos de daño!"

              print(f"\nAtacaste al enemigo por {daño_base_ataque_pesado} puntos de daño.")

        
          case "2" :
            print("\nRáfaga Veloz!")

            for i in range (3):
            
            #Dentro del bucle, en cada repetición: 1. Resta 5 puntos de daño a la vida del enemigo. 

              vida_del_enemigo -= 5

              print("Golpe conectado por 5 de daño.")
        
          case "3" :

            print("\nCurar.")

            # Si tienes pociones (> 0): Suma 30 puntos a tu vida y resta 1 poción. 

            if pociones_de_vida > 0:

              vida_del_gladiador += 30

              pociones_de_vida -= 1

              print("Te curaste 30 puntos.")

              #Si la vida del gladiador supera 100 queda en 100.

              if vida_del_gladiador > 100:

                vida_del_gladiador = 100

              
          
            #Si NO tienes pociones: Muestra "¡No quedan pociones!" y pierdes el turno (el enemigo ataca igual).

            else:

              print("No quedan pociones!")

    print("----------------------------------------------------------------")

    print("Turno del enemigo")

    #Resta el daño base del enemigo (12) a tu vida.

    vida_del_gladiador -= daño_base_del_enemigo

    #Muestra un mensaje: "¡El enemigo te atacó por 12 puntos de daño!"

    print("El enemigo te atacó por 12 puntos de daño!")

    print("----------------------------------------------------------------")

#                   Fin del Juego
# Cuando el ciclo termine (porque la vida de alguno llegó a 0 o menos), debes evaluar: 

# Si vida_jugador > 0: Mostrar "¡VICTORIA! [Nombre] ha ganado la batalla

if vida_del_gladiador > 0 :
       
  print(f"Victoria! {nombre_del_gladiador} ha ganado la batalla.")

# Si vida_jugador <= 0: Mostrar "DERROTA. Has caído en combate.

else:
   
   print("DERROTA. Has caído en combate.")
  

