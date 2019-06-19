from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse
from todo import models
from toodoo import settings


def index(request):
    lists = models.List.objects.all().order_by('-id')

    paginator = Paginator(lists, settings.PER_PAGE)
    page = request.GET.get('p', 1)
    items = paginator.get_page(page)

    context = {
        'items': items,
        'current_page': page,
        'per_page': settings.PER_PAGE
    }

    return render(request, 'index.html', context=context)


def create_list(request):
    return HttpResponse('create_list')
