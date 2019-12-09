from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    content='Index'
    return render(request, 'index.html',{'content': content})