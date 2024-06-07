from django.contrib import admin
from django.utils.translation import gettext_lazy as _
# Register your models here.
from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (_("Title"), {
            "fields": ["title",]
            }),
    ]