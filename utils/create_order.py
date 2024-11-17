import os
import sys
from random import randint
from pathlib import Path
from random import choice

from list_products import products, values_products
 
import django
from django.conf import settings

DJANGO_BASE_DIR = Path(__file__).parent.parent
NUMBER_OF_OBJECTS = 100

sys.path.append(str(DJANGO_BASE_DIR))
os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings' # substitua o 'core' se sua base do projeto tiver outro nome
settings.USE_TZ = False

django.setup()

if __name__ == '__main__':
    import faker

    from orders.models import Order # importe seu model para inserir dados

    Order.objects.all().delete()

    fake = faker.Faker('pt_BR')
    STATUS_CHOICE = ['Aguardando', 'Processando', 'Enviado', 'Entregue', 'Cancelado'] # status disponiveis pode ser removido ou modificado
    django_order = []

    for indc in range(NUMBER_OF_OBJECTS):
        client = fake.profile()

        # indices do obj
        name = client['name']
        product = products[indc]
        amount = randint(0, 100)
        total_price = values_products[indc]
        status = choice(STATUS_CHOICE)

        django_order.append(
            Order(
                client=name,
                product=product,
                amount=amount,
                total_price=total_price,
                status=status,
            )
        )

    if len(django_order) > 0:
        Order.objects.bulk_create(django_order)