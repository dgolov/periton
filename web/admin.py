from django import forms
from django.contrib import admin
from .models import Categories, Products, Applications
from ckeditor.widgets import CKEditorWidget


class ProductsAdminForm(forms.ModelForm):
    characteristics = forms.CharField(label='Характеристики', widget=CKEditorWidget())

    class Meta:
        model = Products
        fields = '__all__'


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}



@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    form = ProductsAdminForm
    list_display = ['name', 'category']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Applications)
class ApplicationsAdmin(admin.ModelAdmin):
    list_display = ['product', 'costumer_name', 'phone', 'created_at']
