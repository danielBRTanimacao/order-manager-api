from ninja import NinjaAPI
from orders.api import orders_router

api = NinjaAPI()
api.add_router('orders/', orders_router)