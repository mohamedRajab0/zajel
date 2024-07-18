# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse  # Add this import statement
from .models import *
from .forms import MessageForms
# Create your views here.

@login_required
def index(request):
    zajel_group = get_object_or_404(ZajelGroup, group_name='puplic-room')
    messages = zajel_group.chat_messages.all()
    form = MessageForms()
    print("Request method:", request.method)
    if request.method == 'POST':
        print('post')
        form = MessageForms(request.POST)
        print("Form data:", form.data)
        if form.is_valid():
            message = form.save(commit=False)
            message.author = request.user
            message.group_name = zajel_group
            message.save()
            context = {
                'message': message,
                'user': request.user,
            }
            return render(request, 'chat_messages.html', context)
    
    context = {
        "form": form,
        "messages": messages,
        "group_name": zajel_group.group_name,  # Pass the group_name to the template
    }
    return render(request, 'index.html', context)
# views.py
from django.contrib.auth import logout



def logout_view(request):
    logout(request)
    return HttpResponse('landing.html')  # Replace 'home' with your desired URL
