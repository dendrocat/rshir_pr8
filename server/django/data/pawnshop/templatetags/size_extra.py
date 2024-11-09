from django import template

register = template.Library()


@register.simple_tag
def convert_size(size):
    marks = ['B', 'KB', 'MB']
    i = 0
    while size > 1024:
        i += 1
        size /= 1024
    return f"{round(size, 2)} {marks[i]}"


