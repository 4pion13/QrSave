from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import NameInfo
# Create your views here.



def home(request):
    name_status = False
    form = NameInfo
    if request.user.is_authenticated:
            lastname = request.user.last_name
            firstname = request.user.first_name
            if "".__eq__(lastname):
                print("Фамилия и имя нема")
                name_status = True
                form = NameInfo(request.POST)
                if form.is_valid():
                        object = User.objects.get(username=request.user)
                        object.last_name = form.cleaned_data['last_name']
                        object.first_name = form.cleaned_data['first_name']
                        object.save()
                        return render(request, 'home.html', {'name_status': name_status, 'form': form})


    else:
        pass


    return render(request, 'home.html', {'name_status': name_status,'form':form})