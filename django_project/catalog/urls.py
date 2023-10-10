from django.urls import path
from django.views.decorators.cache import cache_page

from  catalog.apps import CatalogConfig
from catalog.views import contacts, ProductListView, ProductCreateView, ProductUpdateView, ProductDetailView, \
    ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='update_product'),
    path('<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='delete_product')

]