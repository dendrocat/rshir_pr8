from testsite.utils import get_theme_name
from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def get_theme(context):
    theme = get_theme_name(context['user'])
    return f"css/{theme}.css"