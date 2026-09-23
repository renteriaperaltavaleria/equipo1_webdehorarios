from django.shortcuts import render

# Create your views here.
def pag_inicio(request):
    return render(request, 'pag_inicio.html')
