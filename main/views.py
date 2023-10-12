import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from main.forms import ItemForm
from main.models import Item

@login_required(login_url='/login')
def show_main(request):
  items = Item.objects.filter(user=request.user)
  
  count = items.count()

  context = {
    'nama_mahasiswa': 'Mahartha Gemilang',
    'kelas_mahasiswa': 'PBP D',
    'name': 'Cheese Sauce',
    'amount': '127',
    'description': 'A product made of sauce',
    'count': count,
    'items': items,
    'current_user': request.user,
    'last_login': request.COOKIES['last_login'],
  }

  return render(request, 'main.html', context)

def create_item(request):
  form = ItemForm(request.POST or None)

  if form.is_valid() and request.method == "POST":
    item = form.save(commit=False)
    item.user = request.user
    item.save()
    return HttpResponseRedirect(reverse('main:show_main'))
  
  context = {'form': form}
  return render(request, 'create_item.html', context)

def show_xml(request):
  data = Item.objects.all()
  return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml_by_id(request, id):
  data = Item.objects.filter(pk=id)
  return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
  data = Item.objects.all()
  return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
  data = Item.objects.filter(pk=id)
  return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
  form = UserCreationForm()

  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, 'Your account has been successfully created!')
      return redirect('main:login')
  context = {'form':form}
  return render(request, 'register.html', context)
  
def login_user(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      response = HttpResponseRedirect(reverse("main:show_main")) 
      response.set_cookie('last_login', str(datetime.datetime.now()))
      return response
    else:
      messages.info(request, 'Sorry, incorrect username or password. Please try again.')
  context = {}
  return render(request, 'login.html', context)

def logout_user(request):
  logout(request)
  response = HttpResponseRedirect(reverse('main:login'))
  response.delete_cookie('last_login')
  return redirect('main:login')

def increment_counter(request, id):
  counter = (Item.objects.get(id=id))
  counter.amount += 1
  counter.save()
  return redirect('main:show_main')

def decrement_counter(request, id):
  counter = (Item.objects.get(id=id))
  counter.amount -= 1
  counter.save()
  return redirect('main:show_main')

def delete_item(request, id):
  item = (Item.objects.get(pk=id))
  item.delete()
  return redirect('main:show_main')

def get_item_json(request):
  items = Item.objects.all()
  return HttpResponse(serializers.serialize('json', items))

@csrf_exempt
def add_item_ajax(request):
  if request.method == 'POST':
    name = request.POST.get("name")
    amount = request.POST.get("amount")
    description = request.POST.get("description")
    user = request.user

    new_item = Item(name=name, amount=amount, description=description, user=user)
    new_item.save()

    return HttpResponse(b"CREATED", STATUS=201)
  
  return HttpResponseNotFound()

@csrf_exempt
def increase_item_ajax(request):
  print("BERHASILL")
  if request.method == 'POST':
    id = request.POST.get("id")
    updated = Item.objects.get(pk=id)
    updated.amount += 1
    updated.save()
    return HttpResponse(b"UPDATED", status=201)
  return HttpResponseNotFound()

@csrf_exempt
def decrease_item_ajax(request):
  if request.method == 'POST':
    id = request.POST.get("id")
    updated = Item.objects.get(pk=id)
    if updated.amount > 0:
      updated.amount -= 1
    updated.save()
    return HttpResponse(b"UPDATED", status=201)
  return HttpResponseNotFound()

@csrf_exempt
def delete_item_ajax(request):
  if request.method == 'POST':
    id = request.POST.get("id")
    item = (Item.objects.get(pk=id))
    item.delete()
    return HttpResponse(b"DELETED", STATUS=201)
  return HttpResponseNotFound()