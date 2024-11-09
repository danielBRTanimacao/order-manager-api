from ninja import ModelSchema
from .models import Order
from datetime import datetime

class OrderGetSchema(ModelSchema):
    class Meta:
        model = Order
        fields = "__all__"

class OrderPostSchema(ModelSchema):
    class Meta:
        model = Order
        exclude = "id", "date",