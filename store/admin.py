from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Store)
admin.site.register(Product)
admin.site.register(StoreContent)
admin.site.register(StoreAddProduct)
admin.site.register(StoreBuyProduct)
