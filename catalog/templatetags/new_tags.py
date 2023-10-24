from django import template

register = template.Library()


@register.filter()
def my_image(value):
    if value:
        return f'/image_product/{value}'
    return '#'


@register.simple_tag
def my_image(value):
    return f'/image_product/{value}'