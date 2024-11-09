from ninja import ModelSchema
from .models import Order

class OrderSchema(ModelSchema):
    class Meta:
        model = Order
        exclude = "id", "date",
    