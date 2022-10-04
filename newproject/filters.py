import django_filters
from .models import Car
from django_filters import rest_framework as filters



def filter_by_ids(queryset, name, value):
    values = value.split(',')
    return queryset.filter(name__icontains=values)


class SnippetFilterSet(django_filters.FilterSet):
   name = django_filters.CharFilter(method=filter_by_ids)
    
   class Meta:
      model = Car
      fields = ['name']