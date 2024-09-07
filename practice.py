def menu():
    ejercicio = int(input("Que ejercicio quiere probar?: (0 para salir)"))
    if ejercicio == 1:
        print("Has elegido el Ejercicio 1")
        Ejercicio1()

    elif ejercicio == 2:
        print("Has elegido el Ejercicio 2")
        Ejercicio2()

    elif ejercicio == 3:
        print("Has elegido el Ejercicio 3")
        Ejercicio3()
        
    elif ejercicio == 4:
        print("Has elegido el Ejercicio 4")
        Ejercicio4()

    elif ejercicio == 5:
        print("Has elegido el Ejercicio 5")
        Ejercicio5()

    elif ejercicio == 6:
        print("Has elegido el Ejercicio 6")
        Ejercicio6()

    elif ejercicio == 7:
        print("Has elegido el Ejercicio 7")
        Ejercicio7()

    elif ejercicio == 8:
        print("Has elegido el Ejercicio 8")
        Ejercicio8()

    elif ejercicio == 9:
        print("Has elegido el Ejercicio 9")
        Ejercicio9()

    elif ejercicio == 10:
        print("Has elegido el Ejercicio 10")
        Ejercicio10()

    elif ejercicio == 0:
        print("Saliendo...")
    else:
        print("Ejercicio no válido")

def Ejercicio1():

# Escribe un programa que pida al usuario su nombre y apellido, y luego los imprima juntos en un mensaje de saludo.

    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    print("Su nombre completo es: ", nombre , apellido)

def Ejercicio2():

# Crea una variable llamada precio con el valor 100. Calcula el precio con un descuento del 15% y muestra el precio final.

    precio = 100
    porcentaje = 15
    print(float((precio * porcentaje) / 100))

def Ejercicio3():

# Escribe un programa que pida al usuario su edad y luego determine si es mayor o menor de edad.

    edad = input(int("Ingrese su edad"))
    if edad >= 18:
        print("Eres mayor de edad0")
    else:
        print("Eres menor de edad")

def Ejercicio4():
# Crea un programa que pida al usuario un número y determine si es par o impar.

    num = int(input("Ingrese un numero: "))

    if num % 2 == 0:
        print(num, "Es par")
    else: 
        print(num, "No es par")

def Ejercicio5():
# Escribe un programa que pida al usuario dos números y luego calcule su suma, resta, multiplicación y división.

    num1 = float(input("Ingrese un numero: "))
    num2 = float(input("Ingrese otro numero: "))

    suma = print("Suma: ", num1 + num2)
    resta = print("Resta: ", num1 - num2)
    multiplicacion = print("Multiplicacion: ", num1 * num2)
    divicion = print("Division: ", num1 / num2)

def Ejercicio6():
# Crea un programa que pida al usuario su calificación y luego imprima el mensaje "Aprobado" si la calificación es mayor o igual a 70, o "Reprobado" si la calificación es menor que 70.
    calificacion = float(input("Ingrese su calificaion: "))
    if calificacion >= 70: 
        print("Haz aprobado ", calificacion)
    else: 
        print("NO haz aprobado ", calificacion)

def Ejercicio7():
# Escribe un programa que pida al usuario dos números y luego determine cuál es el mayor.
    numero1 = float(input("Ingrese un numero: "))
    numero2 = float(input("Ingrese otro numero: "))

    if numero1 > numero2: 
        print("El primer numero es mayor que el segundo") 
    elif numero1 < numero2:
        print("El segundo numero es mayor")
    else:
        print("Son iguales")

def Ejercicio8():
# Crea un programa que pida al usuario su nombre y luego imprima un mensaje de bienvenida con su nombre.

    nombre1 = input("Ingrese su nombre ")
    print("Bienvenidid mi bro' ", nombre1)


def Ejercicio9():
# Escribe un programa que pida al usuario un número y luego imprima la tabla de multiplicar de ese número hasta el 10.

    numero = int(input("Ingrese un numero "))
    print(f"Tabla de multiplicar del {numero}:")
    
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

def Ejercicio10():
    numero1 = float(input("Ingrese el primer numero: "))
    numero2 = float(input("Ingrese el segundo numero: "))

    promedio = (numero1 + numero2) / 2

    print(f"El promedio de {numero1} y {numero2} es {promedio}")

menu()