from django.db import models

class Customer(models.Model):
    name = models.TextField() 
    code = models.CharField(max_length=100, unique=True,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        index_together = [['name', 'code']]


class Order(models.Model):
    item = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    time = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
