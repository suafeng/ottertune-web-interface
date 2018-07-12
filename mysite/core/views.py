from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.utils import timezone

from mysite.core.forms import SignUpForm
from mysite.core.models import TpccForm


@login_required
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # benchmark = form.get('benchmark')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('tpcc')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def tpcc(request):
    if request.method == 'POST':
        form = TpccForm(request.POST)
        if form.is_valid():
            return redirect('lead')
    else:
        form = TpccForm()
    return render(request, 'select.html', {'form': form})

def board(request):
    users = User.objects.all()

class LeadListView(ListView):
    model = User
    template_name = 'lead.html'  # Default: <app_label>/<model_name>_list.html
    context_object_name = 'users'  # Default: object_list
    queryset = User.objects.all()