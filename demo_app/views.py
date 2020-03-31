from django.http import HttpResponse
from django.template import loader

from .models import Idea

def index(request):
    idea = Idea(title_en_us='Title en us', content_en_us="Content en us", title_pt_br='Title pt br', content_pt_br="Content pt br")
    idea.save()

    template = loader.get_template('idea/idea.html')
    context = {
        'title': 'Idea Page',
        'idea': idea,
    }
    return HttpResponse(template.render(context, request))

def detail(request, idea_id):
    idea = Idea.objects.get(id=idea_id)
    template = loader.get_template('idea/details.html')
    context = {
        'title': 'Idea Detail Page',
        'idea': idea,
        'idea_id': idea_id,
    }
    return HttpResponse(template.render(context, request))


