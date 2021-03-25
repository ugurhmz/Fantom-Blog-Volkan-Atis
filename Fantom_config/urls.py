
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),  #1.App için urls
    path('users/',include('users.urls')) #2.App (users) için urls

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
