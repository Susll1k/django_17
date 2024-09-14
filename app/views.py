from django.shortcuts import render, redirect
from .models import IceCream
from .forms import IceCreamForm

def home(request):
    icecream = IceCream.objects.all()
    return render(request, 'home.html', {'icecreams': icecream})

def create(request):
    if request.method == 'POST':
        form = IceCreamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = IceCreamForm()
    return render(request, 'create.html', {'form': form})


def success(request):
    return render(request, 'success.html')
