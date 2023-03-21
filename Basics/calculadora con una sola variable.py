print(""" calculadora con una sola variable

================
menu de opciones
================

1.suma
2.resta
3.multiplicacion
4.division
5.modulo
6.potenciacion
7.division entera

=================""")

Opcion = int(input("Que operacion desea ejecutar? = \n"))

numero = float(input("Cual es el primer numero? = \n"))

if Opcion == 1:
    numero += float(input("Cual es el segundo numero? = \n"))
    print(numero)

elif Opcion == 2:
    numero -= float(input("Cual es el segundo numero? = \n"))
    print(numero)

elif Opcion == 3:
    numero *= float(input("Cual es el segundo numero? = \n"))
    print(numero)

elif Opcion == 4:
    numero /= float(input("Cual es el segundo numero? = \n"))
    print(numero)

elif Opcion == 5:
    numero %= float(input("Cual es el segundo numero? = \n"))
    print(numero)

elif Opcion == 6:
    numero **= float(input("Cual es el segundo numero? = \n"))
    print(numero)

elif Opcion == 7:
    numero //= float(input("Cual es el segundo numero? = \n"))
    print(numero)

else:
    print("opcion invalida")

print("fin.")

























    



    
