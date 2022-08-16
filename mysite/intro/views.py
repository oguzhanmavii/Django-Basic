from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse('Merhaba Anasayfa ')


def about(request):
    return HttpResponse('Merhaba Hakkımda')


def settings(request):
    return HttpResponse('Merhaba Ayarlar ')


def exit(request):
    return HttpResponse("Merhaba Çıkış")    