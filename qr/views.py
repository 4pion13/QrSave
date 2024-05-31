from django.shortcuts import render, get_object_or_404, redirect
from .models import InformationAboutBoxes
import qrcode, tempfile, zipfile
import base64
from django.conf import settings
import os
from .forms import InfoBoxes
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#Paginator - инструмент создания нумераций страниц
#EmptyPage - обработка ошибок связанных с не существующим номером страницы
#PageNotAnInteger - обработка ошибок связанных с типом введеных данных в page
from django.http import Http404,QueryDict, FileResponse, HttpResponse, StreamingHttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from django.core.mail import send_mail
from django.views.decorators.http import require_POST
from wsgiref.util import FileWrapper
from django.contrib.auth.decorators import login_required





@login_required
def test(request):
    boxes_info = InformationAboutBoxes.published.all()
    data = "https://pythonist.ru/"
    filename = "site.png"
    img = qrcode.make(data)
    qr_image=True
    form_value = request.POST.copy()
    file_name_list = form_value.getlist('check')
    print(f'РЕЗУЛЬАТ{form_value}')

    if 'download' in form_value:
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

    elif 'print' in request.POST:
        
        return qr_all_print(request, data_list = ",".join(str(element) for element in file_name_list))
        # do something else
        ç
                    #if os.path.exists(path_to_file):
                        #with open(path_to_file, 'rb') as fh:
                            #response = HttpResponse(fh.read(), content_type="application/vnd.png")
                            #response['Content-Disposition'] = 'inline; filename=' + os.path.basename(path_to_file)
                            #return response
                            
                
                    
                    #raise Http404

    return render(request, 'qr/qr_templates/main.html', {'boxesinfo':boxes_info, 'qr_image':qr_image})

@login_required
def qr_detail(request, year, month, day, post, id):
    detail_data = get_object_or_404(InformationAboutBoxes, status=InformationAboutBoxes.Status.PUBLISHED, slug=post, publish__year=year, publish__month=month,
                             publish__day=day, id=id)
    print(year, month, day, post)
    return render(request, 'qr/qr_templates/detail.html', {'detail_data':detail_data})


@login_required
def qr_all_print(request, data_list):
    img_data = data_list.split(",")
    return render(request, 'qr/qr_templates/qr_all_print.html', {'img_data': img_data})


@login_required
def filling_out_forms_about_boxes(request):
    sent = False
    if request.method == 'POST':
        form = InfoBoxes(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            title = cd['title']
            content = cd['content']
            images = cd['img']
            print(title, content, images)
            sent = True

    else:
        form = InfoBoxes()

    return render(request, 'qr/qr_templates/info_about_boxes_input.html', {'form':form, 'status':sent})