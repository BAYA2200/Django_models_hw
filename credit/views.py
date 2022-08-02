from django.shortcuts import render
from random import random, randint
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Client, Credit, Account
# Create your views here.



def randon():
    a = randint(999999999999999, 9999999999999999)
    print(a)


randon()


class ListView(generic.ListView):
    model = Client
    template_name = 'list.html'

class DetailView(generic.DetailView):
    model = Client
    template_name = 'detail.html'
