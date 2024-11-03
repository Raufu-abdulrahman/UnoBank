from django.shortcuts import render

# Create your views here.

def home(reuquest):
    return render(request, 'index.html')
