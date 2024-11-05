from ninja import Router

orders_router = Router()

@orders_router.get('/', response={200: dict})
def index(request):
    return {'ok': 'ok'}