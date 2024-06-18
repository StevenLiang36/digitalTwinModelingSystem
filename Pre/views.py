from django.shortcuts import render


# Create your views here.

def show_model(request):
    return render(request, 'ModelScene.html')
