from django.shortcuts import render, redirect
from django.urls import reverse

from todo.models import List
from todo.forms import ListForm


def index(request):
    items = List.objects.all().order_by('-id')

    return render(request, 'index.html', context={
        'items': items
    })


def create_list(request):
    form = ListForm()

    context = {
        'form': form,
        'action': reverse('store_list')
    }

    return render(request, 'create_list.html', context=context)


def store_list(request):
    form = ListForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():

            List.objects.create(title=request.POST.get('title'))

            return redirect(index)
        else:
            return render(request, 'create_list.html', context={
                'form': form,
                'action': reverse('store_list')
            })
    else:
        return redirect(create_list)


def destroy_list(request, list_id):
    pass


def edit_list(request, list_id):
    try:
        list_item = List.objects.get(id=list_id)
    except List.DoesNotExist:
        return redirect(index)

    form = ListForm()

    return render(request, 'edit_list.html', context={
        'form': form,
        'list': list_item,
        'action': reverse('update_list', kwargs={'list_id': list_id})
    })


def update_list(request, list_id):
    if request.method == 'POST':
        form = ListForm(request.POST)
        try:
            list_item = List.objects.get(id=list_id)
        except List.DoesNotExist:
            return redirect(index)

        if form.is_valid():
            list_item.title = request.POST.get('title')
            list_item.save()
        else:
            return render(request, 'edit_list.html', context={
                'form': form,
                'list': list_item,
                'action': reverse('update_list', kwargs={'list_id': list_item.id})
            })
    return redirect(index)


def create_note(request, list_id):
    pass
