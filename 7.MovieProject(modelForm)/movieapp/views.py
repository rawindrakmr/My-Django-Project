from django.shortcuts import render
from .forms import MoviesForm
from .models import Movie

# Create your views here.
def index_view(request):
    return render(request, 'movieapp/index.html')

def AddMovie(request):
    form=MoviesForm()
    if request.method=='POST':
        form=MoviesForm(request.POST)
        if form.is_valid():
            form.save()
        return index_view(request)
    return render(request,'movieapp/addmovies.html',{'form':form})


def MovieList(request):
    movielist=Movie.objects.all().order_by('-rating')
    return render(request,'movieapp/listmovies.html',{'movielist':movielist})
