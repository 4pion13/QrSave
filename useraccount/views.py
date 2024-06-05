from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required



@login_required
def main(request):
    return render(request, 'useraccount/base.html')



