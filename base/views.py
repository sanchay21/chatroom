from django.shortcuts import render, redirect
from .models import Room, Topic
from .forms import RoomForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

# from django.http import HttpResponse
# Create your views here.

# rooms = [
#     {
#         'id':1,
#         'name':'Python Chatroom'
#     },

#     {
#         'id':2,
#         'name':'BKC..!!'
#     },
#     {
#         'id':3,
#         'name':'Devlopers...ASSEMBLE !!!'
#     },
# ]

def home(request):
    topics = Topic.objects.all()

    if request.method == "GET":
        q = request.GET.get('q', '')
    rooms = Room.objects.filter(topic__name__icontains = q)
        
    context = {'rooms':rooms, 'topics':topics}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room':room}
    return render(request, 'base/room.html', context)

def createRoom(request):
    form = RoomForm()
    context = {'form':form}

    if(request.method == 'POST'):
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'base/room_form.html', context)

def updateRoom(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if(request.method == 'POST'):
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request, 'base/room_form.html', context)

def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    if request.method == "POST":
        room.delete()
        return redirect('home')
    context = {'obj':room.name, 'deleteType':'Room'}
    return render(request, 'base/delete.html', context)

def loginPage(request):

    if(request.method == "POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, 'User Does Not Exist')

        user = authenticate(username=username, password=password)
        
        if (user is not None):
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR Password Does Not Match')
    context = {'obj':'login'}
    return render(request, 'base/login_register.html', context)

def logoutPage(request):
    logout(request)
    return redirect('home')