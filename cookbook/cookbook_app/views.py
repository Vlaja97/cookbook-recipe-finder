from django.shortcuts import render
from django.http import HttpResponse

def base(request):
    content='base'
    return render(request, 'base.html',{'content': content})