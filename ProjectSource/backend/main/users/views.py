from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .forms import UserCreationForm

def login(request):
    if (request.method == 'GET'):
        print('hello get')
        # do something
        form = UserCreationForm()
        return render(request, 'form.html', {'form': form})
    else:
        print('hello post')
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('spots-page')
        return redirect('spots-page')
    
def logout(request):
    return HttpResponse('Logout Page')

def register(request):
    return HttpResponse('Register Page')
