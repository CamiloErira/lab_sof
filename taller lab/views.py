from django.shortcuts import render

def index(request):
    # Puedes implementar lógica adicional aquí para obtener información de productos si es necesario
    return render(request, 'index.html')
