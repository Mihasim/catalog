from django import template

register = template.Library()


@register.filter()
def first_100(value: str):
    text = value[:100]
    return f'{text}...'


@register.filter()
def mediapath(val):
    if val:
        return f'/media/{val}'

    return '/static/photo.jpg'


@register.simple_tag
def mediapath(val):
    if val:
        return f'/media/{val}'

    return '/static/photo.jpg'
