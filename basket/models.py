from django.db import models
from menu.models import Products

from users.models import User


class BasketQuerySet(models.QuerySet):

    def total_price(self):
        return sum(basket.products_price() for basket in self)

    def total_quantity(self):
        if self:
            return sum(basket.quantity for basket in self)

        return 0


class Basket(models.Model):
    session_key = models.CharField(max_length=32, null=True, blank=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Пользователь')
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name='Продукт')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    class Meta:
        db_table = 'basket'
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    objects = BasketQuerySet().as_manager()

    def products_price(self):
        return round(self.product.price * self.quantity)

    def __str__(self):
        return f'Корзина {self.user.username} | Товар {self.product.name} | Количество {self.quantity}'
