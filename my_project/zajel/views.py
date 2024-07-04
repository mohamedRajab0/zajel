from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import MessageForms
# Create your views here.

@login_required
def index(request):
    zajel_group = get_object_or_404(ZajelGroup, group_name='puplic-room')
    messages = zajel_group.chat_messages.all()
    form = MessageForms()
     
    if request.method == 'POST':
        form = MessageForms(request.POST)
       
        if form.is_valid():
            zajel_message = form.save(commit=False)
            zajel_message.author = request.user
            zajel_message.group_name = zajel_group
            zajel_message.save()
            return redirect('index')
    context = {
        "form": form,
        "messages": messages,
    }
    return render(request, 'index.html', context)