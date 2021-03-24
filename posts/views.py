from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from .models import Post

#__________________________________ IndexView(ListView)__________________________

class IndexView(ListView):
    template_name = 'posts/index.html' #templates->posts->index.html
    model = Post
    context_object_name = 'posts'  #key ->value gibi düşünebilirsin.

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView,self).get_context_data(**kwargs)

        return context


#__________________________________ PostDetail(DetailView)__________________________

class PostDetail(DetailView):
    template_name='posts/detail.html'
    model = Post
    context_object_name = 'single'


    def get_context_data(self, **kwargs):
        context= super(PostDetail, self).get_context_data(**kwargs)

        return context

