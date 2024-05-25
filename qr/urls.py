from django.urls import path, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'qr'

urlpatterns = [
    #Урл на основе представления функции
    #path('', views.post_list, name='post_list'),
    #############################################
    path('', views.test, name='test'),
    path('<int:day>/<int:month>/<int:year>/<slug:post>/<int:id>', views.qr_detail, name='qr_detail'),
    path('qr_all/qr/<str:data_list>', views.qr_all_print, name='qr_all'),
    path('new_box/', views.filling_out_forms_about_boxes, name='new_box')
    
    #path('<int:post_id>/share/', views.post_share, name='post_share'),
    #path('<int:post_id>/comment/', views.post_comment, name='post_comment')

]


urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)