from django.http import HttpResponse
from django.shortcuts import redirect, render


def index(request):
    return HttpResponse('ok')


def login(request):
    return redirect('/index')
