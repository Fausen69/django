# Внимание, пременную pk из функции ice_cream_detail
# передавть в шаблон в этом задании не надо.
# Достаточно просто получить ее, как второй обязательный
# аргумент и вызвать соответствующий шаблон
from django.shortcuts import render

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


def ice_cream_detail(request, pk):
    context = {
        'ice_cream': ice_cream_catalog[pk]
    }
    return render(request, 'ice_cream/detail.html', context)


def ice_cream_list(request):
    context = {
        'ice_cream_list': ice_cream_catalog,
    }
    return render(request, 'ice_cream/list.html', context)