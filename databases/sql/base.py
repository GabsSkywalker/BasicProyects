import mysql.connector 

database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    )
cursor = database.cursor(buffered=True)

cursor.execute("""
CREATE DATABASE IF NOT EXISTS proyecto1;
use proyecto1;
CREATE TABLE IF NOT EXISTS usuarios(
    id int(25) auto_increment not null,
    nombre varchar(100),
    apellidos varchar(255),
    email varchar(255) not null,
    password varchar(255) not null,
    fecha date not null,
    CONSTRAINT pk_usuarios PRIMARY KEY(id),
    CONSTRAINT uq_email UNIQUE(email)
)ENGINE=InnoDb;
"""
)

cursor.execute("""
use proyecto1;
CREATE TABLE IF NOT EXISTS notas(
    id int(25) auto_increment not null,
    usuario_id int(25) not null,
    titulo varchar(255) not null,
    descripcion MEDIUMTEXT,
    fecha date not null,
    CONSTRAINT pk_notas PRIMARY KEY(id)
    CONSTRAINT fk_notas FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
)ENGINE=InnoDb;
"""
)