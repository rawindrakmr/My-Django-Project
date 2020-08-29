from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):
    #if you are working with static media/resources
    # dest1=Destination()
    # dest1.name='Mumbai'
    # dest1.img='destination_1.jpg'
    # dest1.desc='The city that never sleeps'
    # dest1.price=100
    # dest1.offer=False

    # dest2=Destination()
    # dest2.name='Kabul'
    # dest2.img='destination_2.jpg'
    # dest2.desc='The city that never sleeps'
    # dest2.price=100
    # dest2.offer=True

    # dest3=Destination()
    # dest3.img='destination_3.jpg'
    # dest3.name='Hydrabad'
    # dest3.desc='The city that never sleeps'
    # dest3.price=100
    # dest3.offer=False

    # dests=[dest1,dest2,dest3]
    dests=Destination.objects.all()
    return render( request,'travelapp/index.html', {'dests':dests}) 