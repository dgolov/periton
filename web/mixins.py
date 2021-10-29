from django.views.generic.detail import SingleObjectMixin
from django.views.generic import View
from .models import Categories, Products



class CategoryMixin(View):

    def dispatch(self, request, *args, **kwargs):
        self.categories = Categories.objects.order_by('name')
        self.products = Products.objects.order_by('name')
        return super().dispatch(request, *args, **kwargs)



class CategoryDetailMixin(SingleObjectMixin):

    def get_context_data(self, **kwargs):
        if isinstance(self.get_object(), Categories):
            context = super().get_context_data(**kwargs)
            context['category'] = self.get_object()
            context['products'] = Products.objects.all()
            return context

        context = super().get_context_data(**kwargs)
        context['category'] = Categories.objects.order_by('name')
        return context