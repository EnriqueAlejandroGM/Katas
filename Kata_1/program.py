# program.py
# Iniciacion de variable que solo suma dos números.
sum = 1 + 2
print("Variable sum", sum)
# El comando print se utiliza para imprimir información en la consola
print('Hola desde la consola.')
# Iniciacion de variable que solo suma dos números para lo siguiente en una nueva variable multiplicar la variable anterior.
product = sum * 2
print("Variable product", product)
# Tipos de variables
planetas_en_el_sistema_solar = 8 # int, plutón era considerado un planeta pero ya es muy pequeño
distancia_a_alfa_centauri = 4.367 # float, años luz
puede_despegar = True
transbordador_que_aterrizo_en_la_luna = "Apollo 11" #string
# Utilizar type() para saber el tipo de dato
print(type(distancia_a_alfa_centauri))
# Operadores: La idea es que tienes un lado izquierdo y uno derecho asi: izq OPERADOR der
left_side = 10
right_side = 5
print(left_side / right_side) # 2
# Fechas
from datetime import date
print(date.today())
#No se pueden sumar dos tipos de datos distintos, a veces hay que parsearlos
print("Today's date is: " + str(date.today()))
#Introduccion de datosm se utiliza input para leer datos que el usuario introduce
print("Bienvenido al programa de bienvenida")
name = input("Introduzca su nombre ")
print("Saludos: " + name)
# Ahora con numeros
print("Calculadora")
first_number = input("Primer número: ")
second_number = input("Segundo número: ")
print(int(first_number) + int(second_number))