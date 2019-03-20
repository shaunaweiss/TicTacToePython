from django.contrib import admin

from .models import Board, Space


admin.site.register(Board)
admin.site.register(Space)

# Register your models here.
# admin.site.register(Space)
# admin.site.register(Choice)