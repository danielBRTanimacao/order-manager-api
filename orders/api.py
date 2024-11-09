from ninja import Router
from .schemas import OrderSchema
from .models import Order
from typing import Optional

orders_router = Router()

@orders_router.get('/', response={200: list, 400: dict})
def index(request, q: Optional[int] = None):
    orders = Order.objects.all()
    if q is not None: 
        if q < 0:
            return [{
                "title": "Value Error",
                "status": 400,
                "detail": "O valor 'q' nao pode ser negativo!"
            }]
        orders = orders[:q]

    return [OrderSchema.from_orm(order).dict() for order in orders]

@orders_router.post('/', response={200: dict, 401: dict})
def create(request, order_schema: OrderSchema):
    order = Order(order_schema)
    return order
    # return {
    #     "title": "Authentication Error",
    #     "status": 401,
    #     "detail": "usuario nao autenticado permissao negada!"
    # }
