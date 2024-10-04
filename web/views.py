from django.views.generic import TemplateView

class Chat(TemplateView):
    template_name = 'index.html'
    
class Game(TemplateView):
    template_name = 'game.html'
