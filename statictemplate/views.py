from django.shortcuts import render
from django.views.generic import TemplateView

class StaticTemplateView(TemplateView):
    template_name = 'statictemplate/default.html'

    def dispatch(self, request, *args, **kwargs):
        name = kwargs.get('name', 'default')
        self.template_name = 'statictemplate/{}.html'.format(name)
        return super(StaticTemplateView, self).dispatch(request, *args, **kwargs)
