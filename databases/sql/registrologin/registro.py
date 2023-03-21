import mysql.connector 

database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "Proyecto1"
    )

cursor = database.cursor(buffered=True)

def registrar():
    infouser= [
    (input("nombre de usuario: "),input("correo electronico: " ),input("password: "))]
    cursor.executemany("INSERT INTO registro values(null,%s,%s,%s)",infouser)
    database.commit

    return infouser




