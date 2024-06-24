from django.shortcuts import render, redirect
from .models import Message

def interactions(request):
    if request.method == 'GET':
        interactions_messages = Message.objects.all()
        return render(request, 'interactions.html', {'interactions_messages': interactions_messages})
    if request.method == 'POST':
        message_content = request.POST.get('message')

        new_message = Message(
            user = request.user,
            content = message_content
        )

        new_message.save()

        return redirect("/interactions")