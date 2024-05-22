from django.urls import path, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'home'

urlpatterns = [
    #Урл на основе представления функции
    #path('', views.post_list, name='post_list'),
    #############################################
    path('', views.home, name='home'),
    
]


urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)