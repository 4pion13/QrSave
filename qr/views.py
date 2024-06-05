from django.shortcuts import render, get_object_or_404, redirect
from .models import InformationAboutBoxes
import qrcode, tempfile, zipfile
import base64
from django.conf import settings
import os, uuid
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
from django.db.models.functions import Lower
from django.http import JsonResponse
from django.shortcuts import HttpResponse


@login_required
def test(request):
    boxes_info = InformationAboutBoxes.objects.filter(author=request.user, status=InformationAboutBoxes.Status.PUBLISHED)
    qr_image=True
    search = False
    inp_value = ''
    form_value = request.POST.copy()
    form_value_get = request.GET.copy()
    file_name_list = form_value.getlist('check')

    if 'search' in request.GET:
        inp_value = request.GET.get('results', 'This is a default value')
        print(inp_value)
        if "".__eq__(inp_value):
            pass
        else:
            boxes_info = InformationAboutBoxes.objects.filter(title__icontains=inp_value, author=request.user,status=InformationAboutBoxes.Status.PUBLISHED)
            search = True

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


    return render(request, 'qr/qr_templates/main.html', {'boxesinfo':boxes_info, 'qr_image':qr_image, 'search':search, 'input':inp_value})

@login_required
def qr_detail(request, box_id):
    detail_data = get_object_or_404(InformationAboutBoxes, status=InformationAboutBoxes.Status.PUBLISHED, box_id=box_id)

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
            current_user = request.user
            print(current_user.id)
            data_save = form.save(commit=False)
            data_save.author = current_user
            data_save.status = InformationAboutBoxes.Status.PUBLISHED
            box_id = uuid.uuid4().hex
            data_save.box_id = box_id
            data = f"http://127.0.0.1:8000/qr/{box_id}/"
            filename = f"{box_id}.png"
            path = f"images/{filename}"
            image = qrcode.make(data)
            image.save(f"qrsave/media/images/{filename}")
            data_save.img = path
            data_save.save()
            form = InfoBoxes()
            sent = True

    else:
        form = InfoBoxes()

    return render(request, 'qr/qr_templates/info_about_boxes_input.html', {'form':form, 'status':sent})