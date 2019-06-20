from django.shortcuts import render, redirect
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
        'form': form
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
                'form': form
            })
    else:
        return redirect(create_list)


def create_note(request, list_id):
    pass


def destroy_list(request, list_id):
    pass
