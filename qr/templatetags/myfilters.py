from django import template
from django.http import QueryDict

register = template.Library()

@register.filter(name='addclass')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg})



@register.filter(name='onchange')
def onchange(value, arg):
    return value.as_widget(attrs={'onchange': arg})


@register.filter
def replace(value, args):
    qs = QueryDict(args)
    return value.replace(qs.get('cherche',''), qs.get('remplacement',''))