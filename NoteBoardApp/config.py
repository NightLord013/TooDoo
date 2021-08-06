class SiteTheme:

    BASE_COLOR = '#FFFFFF'
    USER_COLOR =''

    @classmethod
    def get_color(cls, request):
        if request.session.get('site_color'):
            return request.session.get('site_color')
        else:
            return cls.BASE_COLOR

    @classmethod
    def set_color(cls, request):
        request.session['site_color'] = request.POST['title']
        return 'success'
