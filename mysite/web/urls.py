from django.urls import path
from .views import BaseView, CatalogView, DocumentsView, ContactsView


urlpatterns = [
    path('', BaseView.as_view(), name='home'),
    path('catalog', CatalogView.as_view(), name='catalog'),
    path('documents', DocumentsView.as_view(), name='documents'),
    path('contacts', ContactsView.as_view(), name='contacts'),
]