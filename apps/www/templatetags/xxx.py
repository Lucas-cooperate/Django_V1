from django.template.library import Library

register = Library()


@register.simple_tag()
def my_func(v1, v2, v3):
    return "哈哈哈" + v1 + v2 + v3


@register.inclusion_tag("www/xo.html")
def my_xo(num):
    return {"x1": [item for item in num if item > 22]}


@register.filter
def my_tt(a1,a2):
    return "太阳" + a1 + a2
