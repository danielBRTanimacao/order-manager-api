from ninja import Router
from .schemas import OrderSchema
from .models import Order

orders_router = Router()

@orders_router.get('/', response={200: list[OrderSchema]})
def index(request):
    orders = Order.objects.all()
    return [OrderSchema.from_orm(order) for order in orders]
