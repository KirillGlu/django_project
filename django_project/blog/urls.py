from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

# Настраиваем пути для главной страницы и страницы с обратной связью пользователя

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='blog-list'),
    path('<int:pk>', BlogDetailView.as_view(), name='blog-detail'),
    path('create/', BlogCreateView.as_view(), name='blog-create'),
    path('edit/<int:pk>', BlogUpdateView.as_view(), name='blog-edit'),
    path('delete/<int:pk>', BlogDeleteView.as_view(), name='blog-delete'),
]

