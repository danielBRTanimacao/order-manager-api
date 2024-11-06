from ninja import Schema
from datetime import datetime

class OrderSchema(Schema):
    id: int
    client: str
    product: str
    amount: int
    total_price: float
    status: str
    date: datetime
    