from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView,LogoutView

from django.http import HttpResponseRedirect

from django.urls import reverse
from django.utils.decorators import method_decorator


from .forms import RegisterForm,UserProfileForm
# Create your views here.
from django.views.generic import CreateView, UpdateView
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





