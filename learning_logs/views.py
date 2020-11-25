from django.shortcuts import render
from .models import Topic

def index(request):
    """The home page for learning diary."""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """The page that shows all topics."""
    topics = Topic.object.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html')