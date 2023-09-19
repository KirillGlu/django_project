from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from pytils.translit import slugify

from catalog.models import Product


# def home(request):
#     return render(request, 'catalog/home.html')


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'



class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/products.html'
    context_object_name = 'post'
    pk_url_kwarg = 'pk'


class ProductCreateView(CreateView):
    """
    Контроллер создания поста блога
    """

    model = Product
    fields = ('name', 'category', 'description', 'purchase_price', 'date_of_creation', 'last_modified_date',)
    success_url = reverse_lazy("catalog:product_list")

    # Реализуем динамический slug

    # def form_valid(self, form):
    #     if form.is_valid():
    #         new_product = form.save()
    #         new_product.slug = slugify(new_product.title)
    #         new_product.save()

        # return super().form_valid(form)
# def home(request):
#     products_list = Product.objects.all()
#     context = {
#         'object_list': products_list,
#         'title': 'Главная'
#     }
#     return render(request, 'catalog/home.html', context)




def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} {phone}: {message}')

    context = {
        'title': 'Контакты'
    }

    return render(request, 'catalog/contacts.html', context)
