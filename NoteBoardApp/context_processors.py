from .models import Category
from .config import SiteTheme


def category(request):
    if request.user.is_anonymous:
        return {'categories': ''}
    else:
        return {'categories': Category.objects.filter(user=request.user)}

def site_theme(request):
    return {'site_color': SiteTheme.get_color(request)}