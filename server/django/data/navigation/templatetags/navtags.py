from django import template
from django.urls import reverse_lazy
from django.contrib.auth.models import User

register = template.Library()


@register.simple_tag()
def get_nav_url(item: dict):
    static = item.get("static", False)
    if static:
        return item['url']
    return reverse_lazy(item['url'])


def check_authorization(item: dict, user: User):
    perm = [
        item.get('superuser', False) and not user.is_superuser,
        item.get('staff', False) and not user.is_staff,
        item.get('require_authorization', False) and not user.is_authenticated,
        item.get('without_authorization', False) and user.is_authenticated
    ]
    return not any(perm)

@register.simple_tag(takes_context=True)
def filter_urls(context, urls):
    user = context['user']
    return [url for url in urls if check_authorization(url, user)]
