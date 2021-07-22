from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def index(request):
    pass


def HABCreate(request):
    pass


def HABEdit(request):
    pass


def HABView(request):
    pass


def HABThanks(request):
    pass

