from django.contrib import admin
from .models import book
from .models import take
# Register your models here.
admin.site.register(book)

admin.site.register(take)