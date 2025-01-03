from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict
from django.http import Http404
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

@orders_router.get('/filter', response={200: list[OrderGetSchema]})
def filter_list(
    request, 
    status: str = None,
    product: str = None,
    amount: int = None, 
    price: float = None
):
    orders_filter = Order.objects.all()

    if status is not None:
        orders_filter = orders_filter.filter(status=status)
    
    if product is not None:
        orders_filter = orders_filter.filter(product=product)
    
    if amount is not None:
        orders_filter = orders_filter.filter(amount=amount)
    
    if price is not None:
        orders_filter = orders_filter.filter(total_price=price)

    return orders_filter


@orders_router.get('/{id}', response={200: dict, 400: dict})
def specific_order(request, id: int):
    try:
        order = get_object_or_404(Order, id=id)
        return model_to_dict(order)
    except Http404:
        return raise_detail_message("Nao encontrado", 404, "Encomenda nao encontrada!")

@orders_router.post('/', response={200: dict})
def create(request, order_schema: OrderPostSchema):
    if request.user.is_anonymous:
        return raise_detail_message("Authentication", 401, "Nao tem permissao")
    if Order.objects.filter(**order_schema.dict()).exists():
        return raise_detail_message("Conflict", 409, "Ja registrado!")
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

@orders_unique_router.put('/{id}')
def update(request, id: int, order_schema: OrderPostSchema):
    order_unique = get_object_or_404(Order, id=id)
    for attr, value in order_schema.dict().items():
        setattr(order_unique, attr, value)
    order_unique.save()

    return raise_detail_message("Order update", 200, "Objeto modificado com sucesso")
