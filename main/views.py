from django.shortcuts import render

def show_product(request):
  context = {
    'name': 'Cheese Sauce',
    'amount': '127',
    'description': 'A product made of sauce'
  }

  return render(request, 'main.html', context)