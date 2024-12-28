from django.contrib import admin

# Register your models here.
from .models import Service, Team, Product, Blog, Contact, Plan

admin.site.register(Service)
admin.site.register(Team)
admin.site.register(Product)
admin.site.register(Blog)
admin.site.register(Contact)
admin.site.register(Plan)
