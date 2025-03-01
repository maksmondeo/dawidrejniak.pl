from django.contrib import admin
from .models import *

@admin.register(PdfFile)
class PdfFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'uploaded_at')
    search_fields = ('file',)
    list_filter = ('uploaded_at',)

@admin.register(OdbiorcyZestawu)
class OdbiorcyZestawuAdmin(admin.ModelAdmin):
    list_display = ('imie', 'email', 'uploaded_at')
    list_filter = ('uploaded_at',)
