#GRUPO SALINAS#
#Proyecto de evaluación propedeútico Automation QA")#
#Calculadora#
#Versión: 3.0#
#Alumna: Reyes Trejo Karla Verónica Michelle#

#Imports    
from numpy import *

#Definición de funciones para operaciones
#1 Sumar 
def op_suma():
    acc = 0.0
    print ("Operación Suma, ")
    nparams = int(input("¿cuantos números quieres sumar?: "))
  
    for i in range(nparams): 
        acc =  acc + float(input("ingrese num["+ str(i) + "]: "))
    print("resultado: " + str(acc)) 
#2 Restar
def op_resta():
 print ("Operación Resta, por favor ingresa:")
 s1 = input("Minuendo: ")
 s2 = input("Sustraendo: ")
 print("resultado: " + str(int(s1)- int(s2)))  
#3 Multiplicar 
def op_multiplica():
 parametros = []
 acc = 1.0
 nparams = int(input("Operación Multiplicar, ¿cuantos números quieres multiplicar?: "))
 for i in range(nparams):
    parametros.append(float(input("ingrese multiplicador["+ str(i) + "]: ")))
  
 nparams-=1
 
 while nparams >= 0 :
    acc *= parametros [nparams]
    nparams -= 1
    
 print("resultado: " + str(acc))  

#4 Dividir 
def op_divide():
 print ("Has elegido operación Dividir, por favor ingresa:")
 s1 = input("Dividendo: ")
 s2 = input("Divisor: ")
 print("resultado: " + str(int(s1) / int(s2)))  #hace falta incluir validación de parámetros

#5 Raiz
def op_raiz():
    print ("Has elegido operación raiz cuadrada, ingresa el numero a calcular:")
    s1 = input("Raiz de: ")
    print("resultado: " + str(sqrt(int(s1))))  #hace falta incluir validación de parámetros
 
 #6 Exponente
def op_exp():
    print("Has elegido operación  exponencial, por favor ingresa:")
    s1 = input("la base: ")
    s2 = input("el exponente: ")
    print("resultado: " + str(pow(int(s1),int(s2))))  #hace falta incluir validación de parámetros

#7 Seno
def op_seno():
    print ("Función trigonométrica  Seno: ")
    s1 = input("Número a calcular: ")
    print("resultado: " + str(sin(float(s1))))  #hace falta incluir validación de parámetros

#8 Coseno
def op_cos():
    print ("Función trigonométrica Coseno: ")
    s1 = input("Número a calcular: ")
    print("resultado: " + str(cos(float(s1))))  #hace falta incluir validación de parámetros

#9 Tangente 
def op_tan():
    print ("Función trigonométrica Tangente: ")
    s1 = input("Número a calcular: ")
    print("resultado: " + str(tan(float(s1))))  #hace falta incluir validación de parámetros

#Definición de menú de la calculadora
def mi_menu():
    print("Proyecto de evaluación propedeútico Automation QA [Calculadora v3.0]")
    print("Alumna: Reyes Trejo Karla Verónica Michelle")
    print("1 .- Sumar")
    print("2 .- Restar")
    print("3 .- Multiplicar")
    print("4 .- Dividir")
    print("5 .- Raiz Cuadrada")
    print("6 .- Exponente")
    print("7 .- Función Seno")
    print("8 .- Función Coseno")
    print("9 .- Función Tangente")
    print("0 .- Salir ...")

    opc = int(input("Elige el numero de la operación a realizar:"))

    if opc == 1:
        op_suma()
        input("presiona enter para continuar ...")
        mi_menu()
    elif opc == 2:
        op_resta()
        input("presiona enter para continuar ...")
        mi_menu()
    elif opc == 3: 
        op_multiplica()
        input("presiona enter para continuar ...")
        mi_menu()
    elif opc == 4:
        op_divide()
        input("presiona enter para continuar ...")
        mi_menu()
    elif opc == 5:
        op_raiz()
        input("presiona enter para continuar ...")
        mi_menu()
    elif opc == 6: 
        op_exp()
        input("presiona enter para continuar ...")
        mi_menu()
    elif opc == 7:
        op_seno()
        input("presiona enter para continuar ...")
        mi_menu()
    elif opc == 8:
        op_cos()
        input("presiona enter para continuar ...")
        mi_menu()
    elif opc == 9:
        op_tan()
        input("presiona enter para continuar ...")
        mi_menu()
    elif opc == 0:
        print("Gracias por usar la calculadora...")
    else:
        print("Opcion no válida...")
        input("presiona enter para continuar ...")
        mi_menu()

mi_menu();