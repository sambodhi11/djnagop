from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.views import View
from .models import hello
from .forms import helloForm


def index(request):
    return render(request, 'index.html')

class HelloView(View):
    def get(self, request):
        form = helloForm()
        context = {"form": form}
        return render(request, 'add.html', context)
    
    def post(self, request):
        form = helloForm(request.POST)
        if form.is_valid():
            event_date = form.cleaned_data['date']
            if event_date < timezone.now().date():
                form.add_error('date', "Event date must be today or in the future.")
                context = {"form": form}
                return render(request, 'add.html', context)
            
            form.save()
            #print("Event added.")
            return redirect('display')  
        
        context = {"form": form}
        return render(request, 'add.html', context)

class DisplayView(View):
    def get(self, request):
        events = hello.objects.all()
        return render(request, 'display.html', {'events': events})


class filterView(View):
    def get(self, request, *args, **kwargs):
        active_users = hello.objects.filter(active=True)
        return render(request, 'filter.html', {'active_users': active_users})
