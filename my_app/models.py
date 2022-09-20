from csv import list_dialects
from re import S
from tokenize import String
from xml.dom.expatbuilder import Rejecter
from django.db import models

class Client(models.Model):
    name = models.CharField("Nome", max_length=30)
    doc = models.CharField("CNPJ", max_length=14)
    about = models.TextField("Sobre")
    active = models.BooleanField("Ativo")
    site = models.CharField("Site", max_length=14)

    def __str__(self):
        return "{}".format(self.pk)

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
    clients = []
    for j in list(Client.objects.all()):
        clients.append((str(j.id), str(j.id)))
    clients = tuple(clients)

    costumer = models.CharField(max_length=50, choices=clients, verbose_name = "Cliente id")
    From = models.CharField("De", max_length=30)
    to = models.CharField("Para", max_length = 30)
    initial_value = models.FloatField("Valor inicial", max_length=10)
    value_type = models.CharField("Moeda", choices = type_coins, default = "2", max_length = 4)
    amount = models.FloatField("Quantidade", max_length=10)
    amount_type = models.CharField("Un. de medida", choices = options, default = "1", max_length = 4)

    def __str__(self):
        return f"{self.id}"

class Bid(models.Model):
    provider_ = []
    offert_ = []
    for j in list(Company.objects.all()):
        provider_.append((str(j.id), str(j.id)))

    for k in list(Offert.objects.all()):
        offert_.append((str(k.id), str(k.id)))

    provider_ = tuple(provider_)
    offert_ = tuple(offert_)

    provider = models.CharField(max_length=50, choices=provider_, verbose_name = "Provider id")

    offert = models.CharField(max_length=50, choices=offert_, verbose_name = "Offert id")

    value = models.FloatField("Valor", max_length=10)

    amount = models.FloatField("Quantidade", max_length=10)

    def __str__(self):
        return "{} - {}".format(self.pk, "Bid")