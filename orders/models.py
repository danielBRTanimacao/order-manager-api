from django.db import models

# Create your models here.
class Order(models.Model):
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    STATUS_CHOICES = [
        ('Aguardando', 'Aguardando pagamento'),
        ('Processando', 'Processando'),
        ('Enviado', 'Enviado'),
        ('Entregue', 'Entregue'),
        ('Cancelado', 'Cancelado'),
    ]

    client = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    amount = models.BigIntegerField(default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Aguardando')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Encomenda {self.id} - {self.client}, {self.status}'