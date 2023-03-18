from datetime import datetime

from django.views.generic import ListView, DeleteView
from .models import Post


class PostsList(ListView):
    model = Post
    ordering = '-article'
    template_name = 'news.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_news'] = None
        return context


class PostDetail(DeleteView):
    model = Post
    template_name = 'news2.html'
    context_object_name = 'news'
