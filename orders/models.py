from django.db import models

# Create your models here.
class Order(models.Model):
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    STATUS_CHOICES = [
        ('WAI', 'Aguardando pagamento'),
        ('PRO', 'Processando'),
        ('SHI', 'Enviado'),
        ('DEL', 'Entregue'),
        ('CAN', 'Cancelado'),
    ]

    client = models.CharField(max_length=100) # possivel uso de foreign key aqui Clients
    product = models.CharField(max_length=100) # possivel uso de foreign key aqui Products
    amount = models.BigIntegerField(default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='WAI')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Encomenda {self.id} - {self.client}, {self.status}'