from django.shortcuts import render

# Create your views here.
from .models import message,room
from .form import msgform

def box(request,pk):
    room_name = room.objects.get(id=pk)
    print(f'---room name {room_name}')
    messages = message.objects.all().filter(room=room_name)
    return render(request,'chat.html',{'messages':messages,'room_name':room_name})


def list(request):
    rooms = room.objects.all()
    form = msgform()
    if request.method == 'POST':
        form = msgform(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            form = msgform()

        else:
            print('error')
    return render(request,'room.html',{'rooms':rooms,'form':form})