from django.shortcuts import render

from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import Blog


class BlogListView(ListView):
    """
    Контроллер для отображения всех постов блога на главной странице
    """
    model = Blog
    template_name = 'blog/blog_list.html'
    context_object_name = 'objects_list'

    # Выводим только те посты, у которых статус - опубликовано

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)

        return queryset


class BlogDetailView(DetailView):
    """
    Контроллер для отображения отдельного поста блога
    """
    model = Blog
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'pk'

    # Реализуем счетчик просмотров поста

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)

        self.object.views_count += 1
        self.object.save()

        return self.object


class BlogCreateView(CreateView):
    """
    Контроллер создания поста блога
    """

    model = Blog
    fields = ('title', 'content',)
    success_url = reverse_lazy("blog:blog-list")

    # Реализуем динамический slug

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    """
       Контроллер обновления поста блога
    """
    model = Blog
    fields = ('title', 'content',)
    context_object_name = 'post'
    pk_url_kwarg = 'pk'
    # success_url = reverse_lazy("blog:blog-list")

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)

    # Перенаправляем пользователя на свежую страницу отредактированного поста

    def get_success_url(self):
        return reverse('blog:blog-detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    """
    Контроллер для удаления поста
    """
    model = Blog
    context_object_name = 'post'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy("blog:blog-list")


