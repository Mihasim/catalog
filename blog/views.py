from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ('Heading', 'Content', 'image', 'is_active',)
    success_url = reverse_lazy('blog:list')


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'


class BlogDetailView(DetailView):
    model = Blog


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('Heading', 'slug', 'Content', 'image', 'date_of_creation', 'is_active', 'view_count',)
    success_url = reverse_lazy('blog:list')


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')
