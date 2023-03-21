import mysql.connector
database = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "",
        database = "proyecto1",
        port = 3306
        )

cursor = database.cursor(buffered=True)


class nota2:
    def __init__(self,id_usuario,titulo = "",descripcion = ""):
        self.id_usuario =id_usuario
        self.titulo = titulo
        self.descripcion = descripcion

    def guardar(self):
        sql = "INSERT INTO notas VALUES(null, %s, %s, %s, NOW())"
        nota = (self.id_usuario,self.titulo,self.descripcion)
        cursor.execute(sql,nota)
        database.commit()

        return[cursor.rowcount,self]

    def listar(self):
        sql = f"SELECT * FROM notas WHERE usuario_id = {self.id_usuario}"
        cursor.execute(sql)
        result = cursor.fetchall()
        return [cursor.rowcount,result]


    def eliminar(self):
        sql = f"DELETE FROM notas WHERE usuario_id = {self.id_usuario} AND titulo LIKE '%{self.titulo}%' "
        cursor.execute(sql)
        database.commit()

        return [cursor.rowcount, self]