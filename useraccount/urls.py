from django.urls import path, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'useraccount'

urlpatterns = [
    path('', views.main, name='main'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)