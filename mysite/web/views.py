from django.shortcuts import render
from django.views import View


class BaseView(View):
    """ Базовый класс представлений
    """
    title = 'ООО Перитон'
    url = 'web/index.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.url, context)


class CatalogView(View):
    """ Базовый класс представлений
    """
    title = 'Каталог масел | ООО Перитон'
    url = 'web/catalog.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.url, context)


class DocumentsView(View):
    """ Базовый класс представлений
    """
    title = 'Документы | ООО Перитон'
    url = 'web/documents.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.url, context)


class ContactsView(View):
    """ Базовый класс представлений
    """
    title = 'Контакты | ООО Перитон'
    url = 'web/contacts.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.url, context)