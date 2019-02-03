from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse('<p>Welcome to Home Page</p>')

def pet_detail(request,id):
    return HttpResponse(f'<p>pet_detail view with id {id}')