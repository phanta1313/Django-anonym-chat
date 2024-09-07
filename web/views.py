from django.views.generic import TemplateView
    
class Chat(TemplateView):
    template_name = 'index.html'
    