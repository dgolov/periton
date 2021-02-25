from django.urls import path
from .views import BaseView, CatalogView, DocumentsView, ContactsView, CategoryDetailView, ProductsDetailView


urlpatterns = [
    path('', BaseView.as_view(), name='home'),
    path('catalog', CatalogView.as_view(), name='catalog'),
    path('catalog/<str:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('catalog/<str:ct_model>/<str:slug>/', ProductsDetailView.as_view(), name='offers_detail'),
    path('documents', DocumentsView.as_view(), name='documents'),
    path('contacts', ContactsView.as_view(), name='contacts'),
]