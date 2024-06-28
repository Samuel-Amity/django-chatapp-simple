# chatapp/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # Import messages framework for displaying messages
from .models import Room, Message
from .forms import MessageForm

def home(request):
    return render(request, 'chatapp/home.html')

def services(request):
    return render(request, 'chatapp/services.html')

def contact(request):
    return render(request, 'chatapp/contact.html')

def pricing(request):
    return render(request, 'chatapp/pricing.html')

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'chatapp/room_list.html', {'rooms': rooms})

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # Import messages framework for displaying messages
from .models import Room, Message
from .forms import MessageForm

@login_required
def room_detail(request, room_name):
    room = get_object_or_404(Room, name=room_name)
    room_messages = room.messages.order_by('timestamp')

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            message.room = room
            message.save()
            messages.success(request, 'Your message was posted successfully.')
            return redirect('room_detail', room_name=room.name)
        else:
            messages.error(request, 'Failed to post your message. Please try again.')
    else:
        form = MessageForm()

    return render(request, 'chatapp/room_detail.html', {'room': room, 'messages': room_messages, 'form': form})

@login_required
def delete_message(request, room_name, message_id):
    message = get_object_or_404(Message, id=message_id)
    
    if request.method == 'POST' and request.user == message.user:
        message.delete()
        messages.success(request, 'Message deleted successfully.')
    else:
        messages.error(request, 'Failed to delete the message.')

    return redirect('room_detail', room_name=room_name)


@login_required  # Ensure user is logged in to access this view
def room_new(request):
    if request.method == "POST":
        room_name = request.POST.get('name')
        Room.objects.create(name=room_name)
        return redirect('room_detail', room_name=room_name)
    return render(request, 'chatapp/room_new.html')


# chatapp/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomAuthenticationForm

def custom_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page or a specific URL
                return redirect('home')  # Replace with your desired redirect URL
            else:
                # Handle invalid login
                return render(request, 'chatapp/login.html', {'form': form, 'error': 'Invalid username or password.'})
    else:
        form = CustomAuthenticationForm()
    return render(request, 'chatapp/login.html', {'form': form})


# chatapp/views.py

from django.shortcuts import render, redirect
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('custom_login')  # Redirect to the custom login view after successful signup
    else:
        form = SignUpForm()
    return render(request, 'chatapp/signup.html', {'form': form})

# views.py

from django.contrib.auth import logout
from django.shortcuts import redirect

def custom_logout(request):
    logout(request)
    return redirect('custom_login')  # Redirect to login page after logout


# views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Room

def delete_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    room.delete()
    return redirect('room_list')  # Redirect to the room list page after deletion
