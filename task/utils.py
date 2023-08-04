# utils.py
from django.db.models import F
from django.db.models.functions import Coalesce

def filter_and_order_tasks(queryset, filter_option, sort_option):
    
    if filter_option == 'completed':
        queryset = queryset.filter(completed=True)
    elif filter_option == 'active':
        queryset = queryset.filter(completed=False)
    elif filter_option == 'has-due-date':
        queryset = queryset.exclude(dueDate__isnull=True)

    if sort_option == 'added':
        queryset = queryset.order_by('created')
    elif sort_option == 'dueDate':
        return queryset.order_by(F(sort_option).asc(nulls_last=True))

    return queryset
