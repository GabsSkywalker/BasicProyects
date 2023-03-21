
import usuarios.usuario as modelo
import mysql.connector 
import notas.acciones
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "proyecto1",
    port = 3306
    )

cursor = database.cursor(buffered=True)

class Acciones: 

    
    def registro(self):
        print("ok vamos a registrarte")

        nombre = input("cual es tu nombre?: ")
        apellidos = input("cual es tu apellido?: ")
        email = input("cual es tu email?: ")
        password = input("cual seria la password?: ")
        user = modelo.Usuario(nombre ,apellidos ,email ,password,)
        registro = user.registrar()
        database.commit()

        if registro[0] >= 1:
            print(f"perfecto {registro[1].nombre} te haz registrado con el correo {registro[1].email}")

        else:
            print("no te haz registrado correctamente")

    def login(self):
        print("ok,identificate en el sistema")
    #try:
        email = input("cual es tu email?: ")
        password = input("cual seria la password?: ")
        usuario = modelo.Usuario("","",email,password,)
        login = usuario.identificar()

        if email == login[3]:
            print(f"Bienvenido {login[1]},te haz registrado en el sistema el dia {login[5]}")
            self.proximasAcciones(login)
    #except Exception as e:
        print("Login incorrecto,introduzca bien los datos")
            

    def proximasAcciones(self, usuario):
        Acciones = input(""" 
        ****Acciones Disponibles****
        -Crear nota(crear()
        -Mostrar nota(mostrar)
        -Eliminar nota(eliminar)
        -salir(salir)

        Que desea Hacer?: 
        """)

        acciones= Acciones.lower()
        HazEl = notas.acciones.acciones()
    

        if acciones == "crear":
            HazEl.crear(usuario)
            self.proximasAcciones(usuario)

        elif acciones == "mostrar":
            HazEl.mostrar(usuario)
            self.proximasAcciones(usuario)
        elif acciones == "eliminar":
            HazEl.eliminar(usuario)
            self.proximasAcciones(usuario)
        elif acciones == "salir":
            print(f"Hasta luego,{usuario[1]}")

        elif acciones == "":
            self.proximasAcciones(usuario)