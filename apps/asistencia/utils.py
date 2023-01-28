#Copyright (c) 2022 - present, Daniel Escalona

from io import BytesIO
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
    
#--------------------------------------------------------------------->
def page_400(request, exception):
    return render(request, 'errors/400.html', status=400)
    
def page_403(request, exception):
    return render(request, 'errors/403.html', status=403)

def page_404(request, exception):
    return render(request, 'errors/404.html', status=404)

def page_500(request):
    return render(request, 'errors/500.html')

