from django.shortcuts import render
from django.http import HttpResponse

ice_cream_catalog = [
    {
        'id': 0,
        'title': 'Классический пломбир',
        'description': 'Настоящее мороженое, '
                       'для истинных ценителей вкуса. '
                       'Если на столе появляется пломбир'
                       ' — это не надолго.',
    },
    {
        'id': 1,
        'title': 'Мороженое с кузнечиками',
        'description': 'В колумбийском стиле: мороженое '
                       'с добавлением настоящих карамелизованных кузнечиков.',
    },
    {
        'id': 2,
        'title': 'Мороженое со вкусом сыра чеддер',
        'description': 'Вкус настоящего сыра в вафельном стаканчике.',
    },
]


def ice_cream_list(request):
    context = {
        'ice_cream_catalog': ice_cream_catalog,
    }
    return render(request, 'ice_cream/list.html', context)


def ice_cream_list(request):
    return HttpResponse()
