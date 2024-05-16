from django.shortcuts import render, get_object_or_404
from .models import InformationAboutBoxes
import qrcode, tempfile, zipfile
import base64
from django.conf import settings
import os
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#Paginator - инструмент создания нумераций страниц
#EmptyPage - обработка ошибок связанных с не существующим номером страницы
#PageNotAnInteger - обработка ошибок связанных с типом введеных данных в page
from django.http import Http404,QueryDict, FileResponse, HttpResponse, StreamingHttpResponse
from django.views.generic import ListView
from django.core.mail import send_mail
from django.views.decorators.http import require_POST
from wsgiref.util import FileWrapper

def test(request):
    boxes_info = InformationAboutBoxes.published.all()
    data = "https://pythonist.ru/"
    filename = "site.png"
    img = qrcode.make(data)
    qr_image=True
    form_value = request.POST.copy()
    file_name_list = form_value.getlist('check')
    if request.method == 'POST':
        temp = tempfile.TemporaryFile()
        archive = zipfile.ZipFile(temp, 'w', zipfile.ZIP_DEFLATED)   
            #response = FileResponse(open(path_to_file, 'rb'))
            #return response
        for x, file_name in enumerate(file_name_list):
            path_to_file = str(settings.MEDIA_ROOT) +'/'+ file_name   
            title = get_object_or_404(InformationAboutBoxes, img = file_name)
            test = str(title.title)
            archive.write(path_to_file, f'{test}%d.png' % x) 
        archive.close()
        temp.seek(0)
        wrapper = FileWrapper(temp)
        response = HttpResponse(wrapper, content_type='application/zip')
        response['Content-Disposition'] = 'attachment; filename=qrcodes.zip'

        return response
                    #if os.path.exists(path_to_file):
                        #with open(path_to_file, 'rb') as fh:
                            #response = HttpResponse(fh.read(), content_type="application/vnd.png")
                            #response['Content-Disposition'] = 'inline; filename=' + os.path.basename(path_to_file)
                            #return response
                            
                
                    
                    #raise Http404

    return render(request, 'main.html', {'boxesinfo':boxes_info, 'qr_image':qr_image})


def qr_detail(request, year, month, day, post, id):
    detail_data = get_object_or_404(InformationAboutBoxes, status=InformationAboutBoxes.Status.PUBLISHED, slug=post, publish__year=year, publish__month=month,
                             publish__day=day, id=id)
    print(year, month, day, post)
    return render(request, 'detail.html', {'detail_data':detail_data})
