from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView

from .forms import *
from .models import Post, Category, Tag




#__________________________________ IndexView(ListView)__________________________

class IndexView(ListView):
    template_name = 'posts/index.html' #templates->posts->index.html
    model = Post
    context_object_name = 'posts'  #key ->value gibi düşünebilirsin.

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView,self).get_context_data(**kwargs)
        context['slider_posts'] = Post.objects.all().filter(slider_post=True)

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

#__________________________________ TagDetail(ListView)__________________________

class TagDetail(ListView):
    model = Post
    template_name='tags/tag_detail.html'
    context_object_name='posts'


    def get_queryset(self):
        self.tag = get_object_or_404(Tag, slug=self.kwargs['slug'])
        return Post.objects.filter(tag = self.tag).order_by('id')


    def get_context_data(self,**kwargs):
        context = super(TagDetail,self).get_context_data(**kwargs)
        self.tag = get_object_or_404(Tag, slug=self.kwargs['slug'])
        context['tag'] = self.tag


        return context


#__________________________________ CreatePostView(FormView)__________________________


@method_decorator(login_required(login_url='/users/login'), name="dispatch") #Kullanıcının giriş yapması gerekirkir, ekleyebilsin içerik.
class CreatePostView(CreateView):
        template_name = 'posts/create-post.html'
        form_class = PostCreationForm
        model = Post



        def get_success_url(self):
            return reverse('detail',kwargs={"pk":self.object.pk, "slug":self.object.slug})


        def form_valid(self, form):
            form.instance.user = self.request.user
            form.save()
            tags = self.request.POST.get("tag").split(",") #html'de name="tag" olan

            for tag in tags:
                current_tag = Tag.objects.filter(slug=slugify(tag)) #geçerli olan etiketim


                if current_tag.count() < 1: # 1 den küçükse, demekki daha önce yok.hemen olştur.
                    create_tag = Tag.objects.create(title=tag)
                    form.instance.tag.add(create_tag)

                else:
                    exist_tag = Tag.objects.get(slug=slugify(tag))
                    form.instance.tag.add(exist_tag)


            return super(CreatePostView,self).form_valid(form)



#__________________________________ UpdatePostView(UpdateView)__________________________

@method_decorator(login_required(login_url='/users/login'), name="dispatch")
class UpdatePostView(UpdateView):
    model = Post
    template_name='posts/post-update.html'
    form_class = PostUpdateForm



    #update ettikten sonra detay sayfasına git
    def get_success_url(self):
        return reverse('detail', kwargs={"pk": self.object.pk, "slug": self.object.slug})


    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.tag.clear()

        tags = self.request.POST.get("tag").split(",")  # html'de name="tag" olan

        for tag in tags:
            current_tag = Tag.objects.filter(slug=slugify(tag))  # geçerli olan etiketim

            if current_tag.count() < 1:  # 1 den küçükse, demekki daha önce yok.hemen olştur.
                create_tag = Tag.objects.create(title=tag)
                form.instance.tag.add(create_tag)

            else:
                exist_tag = Tag.objects.get(slug=slugify(tag))
                form.instance.tag.add(exist_tag)

        return super(UpdatePostView, self).form_valid(form)



    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.object.user != request.user:
            return HttpResponseRedirect('/')
        
        
        return super(UpdatePostView, self).get(request, *args, **kwargs)



#__________________________________ DeletePostView(DeleteView)__________________________

@method_decorator(login_required(login_url='/users/login'), name="dispatch")
class DeletePostView(DeleteView):
        model = Post
        success_url  ='/'
        template_name="posts/delete-post.html"


        def delete(self, request, *args, **kwargs):
            self.object = self.get_object()
            if self.object.user == request.user:
                self.object.delete()
                return HttpResponseRedirect(self.success_url)

            else:
                return HttpResponseRedirect(self.success_url)




        def get(self, request ,*args, **kwargs):
            self.object = self.get_object()

            if self.object.user != request.user:
                return HttpResponseRedirect('/')
            
            return super(DeletePostView, self).get(request ,*args, **kwargs)

