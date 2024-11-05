from django.test import TestCase
from ninja.testing import TestClient

from .api import orders_router

# Create your tests here.
class OrdersTest(TestCase):
    def test_get_index_msg_is_ok(self):
        client = TestClient(orders_router)
        response = client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'ok': 'ok'})

    def raise_error_if_is_not_get(self):
        client = TestClient(orders_router)
        response = client.post('/')

        self.assertEqual(response.status_code, 500)