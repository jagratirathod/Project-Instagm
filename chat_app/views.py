from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Chat, Message

# Create your views here.

def home(request):
    return HttpResponse("checking........")


def chat_room(request, room_id):
    chat = get_object_or_404(Chat, id=room_id)
    messages = chat.messages.all()
    return render(request, 'chat_room.html', {'chat': chat, 'messages': messages})

def send_message(request, room_id):
    if request.method == 'POST':
        chat = get_object_or_404(Chat, id=room_id)
        sender = request.user
        message_content = request.POST.get('message_content')
        message = Message.objects.create(chat=chat, sender=sender, content=message_content)
        return HttpResponse({'success': True})
    else:
        return HttpResponse({'success': False, 'error': 'Invalid request method.'})

