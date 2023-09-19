from django.urls import path

from  catalog.apps import CatalogConfig
from catalog.views import contacts, ProductListView, ProductDetailView, ProductCreateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>/', ProductDetailView.as_view(), name='products_detail'),
    path('create/', ProductCreateView.as_view(), name='create'),

]