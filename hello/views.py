from django.shortcuts import render
from django.http import HttpResponse

def hello_text_view(request):
    return HttpResponse("Hello DevOps!")

def hello_html_view(request):
    return render(request, 'hello/home.html')

