from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Room, Topic
from .forms import RoomForm, TopicForm

# Create your views here.
from django.http import HttpResponse

# rooms=[
#     {'id':'1','name':'Learn Python!'},
#     {'id':'2','name':'Learn C#!'},
#     {'id':'3','name':'Learn Java!'}
# ]


def loginPage(request):

    if request.user.is_authenticated:
        return redirect('home')

    if (request.method=='POST'):
        username=request.POST.get('username')
        password=request.POST.get('password')

        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request,"User doesn't exist")

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Username or password doesnt exist!")

    context={}
    return render(request,'baseApp\loginRegister.html',context)

def logoutUser(request):
    logout(request)
    return redirect('home')


def home(request):
    query=request.GET.get('q') if(request.GET.get('q')!=None) else ''
    rooms=Room.objects.filter(
        Q(topic__name__icontains=query) |
        Q(host__username__icontains=query) |
        Q(desc__icontains=query) |
        Q(name__icontains=query)
        )
    topics=Topic.objects.all()
    room_count=rooms.count()
    context={'rooms':rooms, 'topics':topics, 'room_count':room_count}
    return render(request, 'baseApp/home.html', context)

def room(request,id):
    room=Room.objects.get(id=id)
    context={'room':room}
    return render(request, 'baseApp/room.html', context)

@login_required(login_url='loginPage')    
def createRoom(request):
    form=RoomForm()
    if request.method=='POST':
        form=RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'baseApp/roomForm.html',context)

@login_required(login_url='loginPage')
def updateRoom(request,id):
    room=Room.objects.get(id=id)
    form=RoomForm(instance=room)

    if request.user!=room.host:
        return HttpResponse('You are not allowed here!')

    if(request.method=='POST'):
        form=RoomForm(request.POST, instance=room)
        if(form.is_valid()):
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'baseApp/roomForm.html', context)

@login_required(login_url='loginPage')
def deleteRoom(request,id):
    room=Room.objects.get(id=id)
    if request.method=='POST':
        room.delete()
        return redirect('home')
    return render(request,'baseApp/delete.html',{'obj':room})

@login_required(login_url='loginPage')
def addTopics(request):
    topic=TopicForm()
    if request.method=='POST':
        topic=TopicForm(request.POST)
        if topic.is_valid():
            topic.save()
            return redirect('home')
    context={"topic":topic}
    return render(request,'baseApp/topicForm.html',context)