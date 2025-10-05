from django.db import models
# Create your models here.
class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    stripe_payment_intent = models.CharField(max_length=200)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.id} - Paid: {self.paid}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product_name}"
