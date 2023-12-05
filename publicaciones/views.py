from django.shortcuts import render


# Create your views here.
def publicaciones_view(request):
    ctx = {
        'publicaciones' : Publicacion.objets.all()
    }
    return render(request, 'publicaciones.html/', ctx)