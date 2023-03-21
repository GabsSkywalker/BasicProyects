class Persona:
    """
    nombre
    apellido
    altura
    edad"""

    def setnombre(self,nombre):
        self.nombre = nombre

    def getnombre(self):
        return self.nombre

    def setapellido(self,apellido):
        self.apellido = apellido

    def getapellido(self):
        return self.apellido

    def setaltura(self,altura):
        self.altura = altura

    def getaltura(self):
        return self.altura

    def setedad(self,edad):
        self.edad = edad

    def getedad(self):
        return self.edad

    def caminar(self):
        return "estoy caminando"

    def hablar(self):
        return "estoy hablando"

    def dormir(self):
        return "estoy durmiendo"

class Informatico(Persona):
    def __init__(self):
        self.lenguajes = "HTML,CSS,JavaScript"
        self.experiencia = "5 years"
    
    def getlenguajes(self):
        return self.lenguajes

    def aprender(self,lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes

    def programar(self):
        return "estoy programando"

    def RepararPc(Self):
        return "Estoy Reparando la PC "


class TecnicoRedes(Informatico):
    def __init__(self):
        super().__init__()
        self.auditaredes = "experto"
        self.experienciaredes="15 years"

    def auditar(self):
        return "estoy auditando"

        
