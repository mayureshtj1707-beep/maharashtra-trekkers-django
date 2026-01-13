from django.contrib import admin

# Register your models here.
from .models import Trek, Booking

admin.site.register(Trek)
admin.site.register(Booking)
