from django.contrib import admin
from .models import Jobs, Workers, Storage, Menu, Order

admin.site.register(Jobs)
admin.site.register(Workers)
admin.site.register(Storage)
admin.site.register(Menu)
admin.site.register(Order)
# Register your models here.
