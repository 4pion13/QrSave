from django.shortcuts import render, get_object_or_404
from .models import InformationAboutBoxes
import qrcode
import base64
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#Paginator - инструмент создания нумераций страниц
#EmptyPage - обработка ошибок связанных с не существующим номером страницы
#PageNotAnInteger - обработка ошибок связанных с типом введеных данных в page
from django.http import Http404
from django.views.generic import ListView
from django.core.mail import send_mail
from django.views.decorators.http import require_POST

def test(request):
    boxes_info = InformationAboutBoxes.published.all()
    data = "https://pythonist.ru/"
    filename = "site.png"
    img = qrcode.make(data)
    qr_image=True
    return render(request, 'main.html', {'boxesinfo':boxes_info, 'qr_image':qr_image})


def qr_detail(request, year, month, day, post, id):
    detail_data = get_object_or_404(InformationAboutBoxes, status=InformationAboutBoxes.Status.PUBLISHED, slug=post, publish__year=year, publish__month=month,
                             publish__day=day, id=id)
    print(year, month, day, post)
    return render(request, 'detail.html', {'detail_data':detail_data})
