print("""
==================================================================
Calculo de dias de vacaciones de empleados de  multinacional Rappi
==================================================================\n
""")

nombre = input("Escriba el nombre del Trabajador: \n")
clave = int(input("Escriba la clave del trabajador: \n"))
tiempo = float(input("escriba cuantos Año tiene el trabajador en la empresa: \n"))

if clave == 1:
    if tiempo >= 1 and tiempo <= 2:
        print ("\n El señor",nombre,"tiene derecho a 6 dias de vacaciones")

    elif tiempo >= 2 and tiempo <= 6:
         print ("\n El señor",nombre,"tiene derecho a 14 dias de vacaciones")

    elif tiempo >= 7:
         print ("\n El señor",nombre,"tiene derecho a 20 dias de vacaciones")

elif clave == 2:
        if tiempo >= 1 and tiempo <= 2:
            print ("\n El señor",nombre,"tiene derecho a 7 dias de vacaciones")

        elif tiempo >= 2 and tiempo <= 6:
            print ("\n El señor",nombre,"tiene derecho a 15 dias de vacaciones")

        elif tiempo >= 7:
            print ("\n El señor",nombre,"tiene derecho a 22 dias de vacaciones")

elif clave == 3:
        if tiempo >= 1 and tiempo <= 2:
            print ("\n El señor",nombre,"tiene derecho a 10 dias de vacaciones")

        elif tiempo >= 2 and tiempo <= 6:
            print ("\n El señor",nombre,"tiene derecho a 20 dias de vacaciones")

        elif tiempo >= 7:
            print ("\n El señor",nombre,"tiene derecho a 30 dias de vacaciones")
    
else:
    print("clave invalida")






