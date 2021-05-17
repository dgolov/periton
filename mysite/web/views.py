from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.views import View
from django.views.generic import DetailView
from .models import Categories, Products, Applications
from .mixins import CategoryMixin, CategoryDetailMixin
from .forms import ApplicationForm


class BaseView(View):
    """ Базовый класс представлений
    """
    title = 'ООО Перитон'
    url = 'web/index.html'

    def get(self, request, *args, **kwargs):
        context = {'title': self.title}
        return render(request, self.url, context)


class CatalogView(CategoryMixin, View):
    """ Базовый класс представлений
    """
    title = 'Каталог масел | ООО Перитон'
    url = 'web/catalog.html'

    def get(self, request, *args, **kwargs):
        context = {
            'title': self.title,
            'categories': self.categories,
            'products': self.products
        }
        return render(request, self.url, context)


class DocumentsView(View):
    """ Базовый класс представлений
    """
    title = 'Документы | ООО Перитон'
    url = 'web/documents.html'

    def get(self, request, *args, **kwargs):
        context = {'title': self.title}
        return render(request, self.url, context)


class ContactsView(View):
    """ Базовый класс представлений
    """
    title = 'Контакты | ООО Перитон'
    url = 'web/contacts.html'

    def get(self, request, *args, **kwargs):
        context = {'title': self.title}
        return render(request, self.url, context)


class CategoryDetailView(CategoryDetailMixin, DetailView):
    """ Представление раздела конкретной категории офферов
    """
    model = Categories
    queryset = Categories.objects.all()
    context_object_name = 'category'
    template_name = 'web/category_detail.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProductsDetailView(DetailView):
    """ Представление раздела конкретного оффера
    """
    context_object_name = 'product'
    template_name = 'web/products_detail.html'
    slug_url_kwarg = 'slug'

    def dispatch(self, request, *args, **kwargs):
        self.queryset = Products._base_manager.all()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ct_model'] = Products._meta.model_name
        context['category'] = Categories.objects.order_by('name')
        context['form'] = ApplicationForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ApplicationForm(request.POST)
        product = Products.objects.get(slug=kwargs.get('slug'))
        if form.is_valid():
            app = Applications.objects.create(**form.cleaned_data, product_id=product.pk)
            send_mail(
                'Сообщение обратной связи "Periton-oil"',
                f"{app.costumer_name}\nНомер телефона: {app.phone}\nСообщение из раздела: {app.product}\n{app.message}",
                'mail@periton-oil.ru', ['dgolov@icloud.com'], fail_silently=False
            )
            messages.add_message(request, messages.INFO, 'Ваше сообщение успешно отправлено')
        else:
            messages.add_message(request, messages.ERROR, 'Ваше сообщение не было отправлено')
        return HttpResponseRedirect('/')
