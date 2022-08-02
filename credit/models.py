from django.db import models


# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True, verbose_name="Имя", help_text="Введите имя")
    citizenship = models.CharField(max_length=20, null=True, blank=True, verbose_name='Гражданство', default='кыргызстан')
    birth_year = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    work_place = models.CharField(max_length=30, null=True, blank=True, verbose_name='Место работы')
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
        db_table = 'customers'

    def __str__(self):
        return self.name


class Account(models.Model):
    number = models.CharField(max_length=16, null=True, blank=True, verbose_name='номер аккаунта', unique=True)
    account_type = models.IntegerField(default=1, null=True, blank=True, verbose_name='тип аккаунта')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')

    class Meta:
        verbose_name = "Аккаунт"
        verbose_name_plural = "Аккаунт"
        db_table = "accounts"

    def __str__(self):
        return self.account_type


class Credit(models.Model):
    sum = models.IntegerField(verbose_name='Сумма кредита', null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name='Аккаунт')

