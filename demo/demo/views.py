from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.utils import timezone

from .forms import SignUpForm
from .models import KnobCatalog, Lead, Config
from django.views.decorators.csrf import csrf_exempt
from django.template.context_processors import csrf


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

@csrf_exempt
def tpcc(request):

    if request.method == 'POST':
        knobs_setting = {}
        #return redirect('lead')
        post = request.POST
        for k in post:
            if k != "username" and k != "email":
                print k
                knobs_setting[k] = post[k]
        config = Config.objects.create(username = post["username"],
                                      email = post["email"],
                                      knobs_setting = knobs_setting)
        config.save()
        print knobs_setting

    knobs = KnobCatalog.objects.all()
    settings = []
    for knob in knobs:
        settings.append((knob, knob.setting.split(",")))
    
    return render(request, 'select.html', {"knobs": settings})

# class LeadListView(ListView):
#     model = User
#     template_name = 'lead.html'  # Default: <app_label>/<model_name>_list.html
#     context_object_name = 'users'  # Default: object_list
#     queryset = User.objects.all()

def lead(request):
    leads = Lead.objects.all()
    return render(request, 'lead.html', {'leads': leads})

'''
class LeadListView(ListView):
    model = Lead
    template_name = 'lead.html'  # Default: <app_label>/<model_name>_list.html
    context_object_name = 'leads'  # Default: object_list
    # queryset = Lead.objects.all()
    leads = Lead.objects.order_by('-throughput')
    curr_rank = 1
    cnt = 0

    for lead in leads:
        if cnt < 1:
            lead.rank = curr_rank
        else:
            if lead.throughput == leads[cnt - 1].throughput:
                lead.rank = leads[cnt - 1].rank
            else:
                curr_rank += 1
                lead.rank = curr_rank
        cnt += 1
    queryset = leads
'''
