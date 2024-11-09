from testsite.utils import get_theme_name

def get_theme(request):
    theme = get_theme_name(request.user)
    return {'theme' : f"css/{theme}.css"}