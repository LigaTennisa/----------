from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
import requests
from .forms import RegisterForm


base_api_url = getattr(settings, 'BASE_API_URL', '')

def index(request):
    response = requests.get(f'{base_api_url}/users', auth=('admin', 'admin'))
    if response.status_code == 200:
        return render(request, "users/index.html", {
            # "users": json.loads(response.content),
            # "subtitle": "Список пользователей"
        })
    else:
        return HttpResponse('Ошибка при получении данных')
    

def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            requests.post('base_api_url',  data = form)
    form = RegisterForm()
    data = {
        'form' : form
    }
    return render(request, 'registration.html', data)

def login(request): 
    return render(request, "login.html")
