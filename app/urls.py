from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('orders/', views.orders_view, name='orders'),
]
