from django.db import models

class Client(models.Model):
    name = models.CharField("Nome", max_length=30)
    doc = models.CharField("CNPJ", max_length=14)
    about = models.TextField("Sobre")
    active = models.BooleanField("Ativo")
    site = models.CharField("Site", max_length=14)

    def __str__(self):
        return "{} - {}".format(self.pk, self.name)

class Company(models.Model):
    name = models.CharField("Nome", max_length=30)
    doc = models.CharField("CNPJ", max_length=14)
    about = models.TextField("Sobre")
    active = models.BooleanField("Ativo")
    site = models.CharField("Site", max_length=14)

    class Meta:
        ordering = ["-name"]
        verbose_name_plural = "Companies"

    def __str__(self):
        return "{} - {}".format(self.pk, self.name)

class Offert(models.Model):
    options = (
        ('1', 'ton'),
        ('2', 'kg'),
        ('3', 'g'),
        ('4', 'un'),
    )
    type_coins = (
        ('1', '$'),
        ('2', 'R$'),
    )
    id_costumer = models.ForeignKey(Client, on_delete = models.CASCADE, verbose_name = "ID Cliente")
    From = models.CharField("De", max_length=30)
    to = models.CharField("Para", max_length = 30)
    initial_value = models.FloatField("Valor inicial", max_length=10)
    value_type = models.CharField("Moeda", choices = type_coins, default = "2", max_length = 4)
    amount = models.FloatField("Quantidade", max_length=10)
    amount_type = models.CharField("Un. de medida", choices = options, default = "1", max_length = 4)

    def __str__(self):
        return "{} - {}".format(self.pk, self.name)