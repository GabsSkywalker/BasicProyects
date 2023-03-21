import notas.nota as modelo

class acciones:
    def crear(self,usuario):
        print(f"Ok,{usuario[1]} vamos a crear una nota")
        titulo = input("Cual sera el Titulo?: ")
        descripcion = input("Cual sera la Descripcion?: ")
        nota3 = modelo.nota2(usuario[0],titulo,descripcion)
        guardar = nota3.guardar()

        if guardar[0] >= 1:
            print(f"\nperfecto haz guardado la nota {nota3.titulo}")

        else:
            print(f"Lo sentimos {usuario[1]},no se ha podido guardar la nota")

    def mostrar(self,usuario):
        print(f"\nOk, {usuario[1]}!!! Aqui tienes tus notas: ")
        nota = modelo.nota2(usuario[0]) 
        notas = nota.listar()
        print(notas[0])
        for Mnotas in notas:
            print("--------------------------------------------------------")
            print("Titulo:")
            print(Mnotas[2])
            print("Contenido:")
            print(Mnotas[3])
            print("--------------------------------------------------------")

    def eliminar(self,usuario):
        print(f"Ok,{usuario[1]},vamos a eliminar la nota")
        titulo = input("introduce el titulo de la nota a borrar: ")
        nota = modelo.nota2(usuario[0],titulo)
        eliminar = nota.eliminar()
        if eliminar[0] >= 1:
            print(f"hemos borrado la nota : {nota.titulo}")
        else:
            print("no se ha borrado la nota, prueba luego")



        
