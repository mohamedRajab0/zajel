from django.shortcuts import render
from .models import *
from .forms import MessageForms
# Create your views here.

def index(request):
    form = MessageForms()
    messages = ZajelMessage.objects.all()
    if request.method == 'POST':
        form = MessageForms(request.POST)
        form.instance.author = request.user
        if form.is_valid():
            form.save()
    context = {
        "form": form,
        "messages": messages,
    }
    return render(request, 'index.html', context)