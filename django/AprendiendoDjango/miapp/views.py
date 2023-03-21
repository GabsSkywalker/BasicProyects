from django.shortcuts import render , HttpResponse, redirect
from miapp.models import article 

# Create your views here.
layout = """
<h1>Sitio Web</h1>
<hr/>
<ul>
    <li>
        <a href="/inicio/">Inicio</a>
    </li>
    <li>
        <a href="/pagina/">pagina</a>
    </li>
    <li>
        <a href="/hola-mundo/">hola mundo</a>
    </li>
</ul>
<hr/>
 """



def hola_mundo(request):
    return render(request,'hola_mundo.html')

nombre = "Dans Cheese"
lenguajes = ['python','javascript','php','C']
year = 2023
range = range(year,2051)


def index(request):
    return render(request,'index.html',{
        'title' : 'Inicio',
        'variable' : "soy un dato sexy",
        'nombre' : nombre,
        'lenguajes' : lenguajes,
        'years' : range})
        

def pagina(request,redirigir = 0):

    if redirigir == 1:
       return redirect('contacto',nombre="gabriel",apellido="lemin")

    return render(request,'pagina.html',{
        'texto' : '',
        'lista' : ['1','2','3','4']

    }
                  )

def contacto(request,nombre= "",apellido= ""):
    espacio=" "
    return HttpResponse(layout + f"<h1>Hola,{nombre}{espacio}{apellido}</h1>")

def Crear_Articulo(request,title,content,public):
    articulo = article(
        title = title,
        content = content,
        public = public
    )

    articulo.save()
    return HttpResponse(f"Articulo Creado: {articulo.title} - {articulo.content}")

def articulo(request):
    try:
        articulo = article.objects.get(pk=4,public=True)
        response = f"articulo: {articulo.title} "
    except:
        response = f"Archivo no encontrado"

    return HttpResponse(response)

def editar_articulo(request,id):
    articulo = article.objects.get(pk=id)

    articulo.title = "Batman"
    articulo.content= "Pelicula Del 2017"
    articulo.public = True

    articulo.save()

    return HttpResponse(f"Articulo editado: {articulo.title} - {articulo.content}")


def listar_articulo(request):
        articulo = article.objects.order_by('id')[2:4]
    
        return render(request,'articulos.html',{
        "articulos" : articulo,


        }
                    )

