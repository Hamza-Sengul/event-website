from django import template

register = template.Library()

@register.filter
def yildiz_olustur(puan):
    return '★' * puan
