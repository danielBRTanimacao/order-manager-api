from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {'title': 'index'})

def orders_view(request):
    return render(request, 'orders.html', {'title': 'pedidos'})