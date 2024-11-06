from ninja import Router
from .schemas import OrderSchema
from .models import Order
from typing import List, Optional

orders_router = Router()

@orders_router.get('/', response={200: List[OrderSchema]})
def index(request, q: Optional[int] = None):
    orders = Order.objects.all()
    if q is not None: orders = orders[:q]
    return [OrderSchema.from_orm(order) for order in orders]