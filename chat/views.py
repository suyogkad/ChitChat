from django.shortcuts import render
from .models import Message

# View to display chat messages
def message_list(request):
    # Fetch all messages from the database
    messages = Message.objects.all()

    # Render the message list templates with the messages
    return render(request, 'chat/message_list.html', {'messages': messages})
