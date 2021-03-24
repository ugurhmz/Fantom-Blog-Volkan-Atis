from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView, DetailView
from .models import Post, Category

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



#__________________________________ CategoryDetail(ListView)__________________________

class CategoryDetail(ListView):
    model = Post # Postları listeyeceğiz
    template_name = 'categories/category_detail.html'
    context_object_name = 'posts'


    def get_queryset(self):
        self.category= get_object_or_404(Category,pk=self.kwargs['pk'])
        return Post.objects.filter(category=self.category).order_by('-id')



    def get_context_data(self, **kwargs):
        context= super(CategoryDetail, self).get_context_data(**kwargs)
        self.category = get_object_or_404(Category,pk=self.kwargs['pk'])
        context['category'] = self.category


        return context