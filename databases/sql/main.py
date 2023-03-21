import mysql.connector 
from usuarios import acciones
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "proyecto1",
    port = 3306
    )
cursor = database.cursor(buffered=True)
print("""
    Acciones Disponibles
    -Registro
    -Login
""")
doit=acciones.Acciones()
accion = input("Que desea hacer?: ".lower())
if accion == "registro":
    doit.registro()
elif accion == "login":
    doit.login()