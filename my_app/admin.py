from django.contrib import admin
from .models import Client, Company, Offert, Bid

admin.site.register(Client)
admin.site.register(Company)
admin.site.register(Offert)
admin.site.register(Bid)