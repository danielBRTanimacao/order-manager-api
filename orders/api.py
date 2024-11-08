from ninja import Router
from .schemas import OrderSchema
from .models import Order
from typing import List, Optional

orders_router = Router()

@orders_router.get('/', response={200: List[OrderSchema]})
def index(request, q: Optional[int] = None):
    orders = Order.objects.all()
    if q is not None: 
        # if q < 0:
        #     return [OrderSchema] erro aqui
        orders = orders[:q]
    return [OrderSchema.from_orm(order) for order in orders]

@orders_router.post('/', response={201: List[OrderSchema]})
def create(request, order: OrderSchema):
    if request.user.is_authenticated:
        return order
    return {
        "title": "Raise error authentication",
        "ResponseStatus": 401,
        "detail": "Erro: Não autorizado usuario não autenticado!"
    }