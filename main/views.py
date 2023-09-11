from django.shortcuts import render

def show_product(request):
  context = {
    'nama_mahasiswa': 'Mahartha Gemilang',
    'kelas_mahasiswa': 'PBP D',
    'name': 'Cheese Sauce',
    'amount': '127',
    'description': 'A product made of sauce'
  }

  return render(request, 'main.html', context)