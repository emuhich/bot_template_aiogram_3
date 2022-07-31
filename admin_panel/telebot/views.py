import datetime

from django.shortcuts import render
from django.utils import timezone
from dateutil.relativedelta import relativedelta


def statistics(request):
    template = 'statistics/index.html'

    context = {
        'products_in_work': 0,
        'client_with_subscribe': 0,
        'count_clients': 0,
        'count_chats': 0,
        'count_clients_week': 0,
        'count_clients_today': 0,
        'count_clients_months': 0,
    }

    return render(request, template, context)
