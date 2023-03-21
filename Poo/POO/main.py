from clases import *


persona = Persona()
persona.setnombre("Gabriel")
persona.setapellido("Garcia")
persona.setaltura("1.70")
persona.setedad("20")

print(f"la persona es: {persona.getnombre()} {persona.getapellido()}")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

informatico = Informatico()


informatico.setnombre("Manolo")
informatico.setapellido("Martinez")
print(f"la persona es: {informatico.getnombre()} {informatico.getapellido()}")
print(informatico.programar())

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

tec_redes =  TecnicoRedes()

tec_redes.setnombre("Alfonso")
tec_redes.setapellido("Mejia")
print(f"la persona es: {tec_redes.getnombre()} {tec_redes.getapellido()}")
print(tec_redes.auditar())
print(tec_redes.programar())
