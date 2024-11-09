from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict
from ninja import Router
from .schemas import OrderGetSchema, OrderPostSchema
from .models import Order
from typing import Optional

from utils.raise_errors import raise_detail_message

orders_router = Router()
orders_unique_router = Router()

@orders_router.get('/', response={200: list[dict], 400: dict})
def list_orders(request, q: Optional[int] = None):
    orders = Order.objects.all()
    if q is not None: 
        if q < 0: return [raise_detail_message("Value Error", 400, "O valor 'q' nao pode ser negativo!")]
        orders = orders[:q]
    return [OrderGetSchema.from_orm(order).dict() for order in orders]

@orders_router.get('/{id}', response={200: dict, 400: dict})
def specific_order(request, id: int):
    order = get_object_or_404(Order, id=id)
    return model_to_dict(order)

@orders_router.post('/', response={200: dict})
def create(request, order_schema: OrderPostSchema):
    if request.user.is_anonymous:
        return raise_detail_message("Authentication", 401, "Nao tem permissao")
    new_order = Order(**order_schema.dict())
    new_order.save()
    return raise_detail_message("Created success", 201, "Encomenda criada com sucesso")

@orders_unique_router.delete('/{id}')
def delete(request, id: int):
    if request.user.is_anonymous:
        return raise_detail_message("Authentication", 401, "Nao tem permissao")
    delete_order = get_object_or_404(Order, id=id)
    delete_order.delete()
    return raise_detail_message("Order deleted", 200, "Objeto deletado com sucesso")

# @orders_unique_router.put('/{id}')
# def delete(request, id: int):
#     return raise_detail_message("Order deleted", 200, "Objeto deletado com sucesso")

