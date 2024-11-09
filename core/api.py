from ninja import NinjaAPI
from orders.api import orders_router, orders_unique_router

import orjson
from ninja.parser import Parser

class ORJSONParser(Parser):
    def parse_body(self, request):
        return orjson.loads(request.body)

api = NinjaAPI(parser=ORJSONParser())
api.add_router('orders/', orders_router)
api.add_router('order/', orders_unique_router)