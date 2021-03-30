from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView,LogoutView

from django.http import HttpResponseRedirect

from django.urls import reverse
from django.utils.decorators import method_decorator

from posts.models import Post
from .forms import RegisterForm,UserProfileForm
# Create your views here.
from django.views.generic import CreateView, UpdateView, ListView
from .models import UserProfile


class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = RegisterForm
    success_url = '/' # işlem başarılı login page olana kadar, buraya gitsin.


class UserLogin(LoginView):
    template_name='users/login.html'


class UserLogout(LogoutView):
    template_name = 'users/logout.html'


@method_decorator(login_required(login_url='users/login'), name='dispatch')
class UserProfileUpdateView(UpdateView):
    model = UserProfile
    template_name = 'users/profile-update.html'
    form_class = UserProfileForm


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(UserProfileUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('users:update_profile', kwargs={'slug': self.object.slug})

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user != request.user:
            return HttpResponseRedirect('/')
        return super(UserProfileUpdateView, self).get(request, *args, **kwargs)


@method_decorator(login_required(login_url='users/login'), name='dispatch')
class  UserProfileView(ListView):
    template_name = 'users/my-profile.html'
    model = Post
    context_object_name ='userposts'
    paginate_by = 5


    #ekstra context'imiz, userı çekeceğimiz
    def get_context_data(self,**kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context['userprofile'] = UserProfile.objects.get(user=self.request.user)#giriş yapmış kullanıcının profilini getir bana.
        return context


    # O KULLANICIYA AİT POSTLARI ÇEKMEK İÇİN :
    def get_queryset(self):
        return Post.objects.filter(user=self.request.user).order_by('-id')



#_____________________________ UserPostView(ListView)__________________________________________
class UserPostView(ListView):

    template_name ='users/users-posts.html'
    model = Post
    context_object_name = 'posts'
    paginate_by = 5
    #Yukarısı komple bütün postları çeker

    #Aşağıda ise kullanıcıya ait postları çekme:
    def get_queryset(self):
        return Post.objects.filter(user = self.kwargs['pk']) #Gelen kullanıcının id'sini tarayıcıya koyup, o id ye göre


#_____________________________ UserListView(ListView)__________________________________________
class UserListView(ListView):
    template_name ='users/user-list.html'
    model = UserProfile
    context_object_name = 'users' # html templatesinde -> users olarak kullanacaz..
    paginate_by = 5


    def get_context_data(self, *, object_list=None, **kwargs):
        context= super(UserListView, self).get_context_data(**kwargs)
        return context

















