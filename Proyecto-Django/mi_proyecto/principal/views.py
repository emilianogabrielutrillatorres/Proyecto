from django.shortcuts import render

def inicio(request):
    return render(request, 'inicio.html', {
        'titulo': 'Bienvenido a mi proyecto Django'
    })

def acerca(request):
    return render(request, 'acerca.html', {
        'nombre': 'Gerson Rivera',
        'proposito': 'Este proyecto fue creado como trabajo final para practicar Django'
    })
