from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth import views, logout, login
from django.contrib.auth.decorators import login_required
from django.template.context_processors import request
from django.http import HttpResponseRedirect
import time, datetime, string
from .models import G
from .forms import GForm, UserForm

# Create your views here.
def home(request):
    return render(request,"home.html")


def u_new(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            #new_user = UserForm.Users.objects.create_user(**form.cleaned_data)
            form.save()
            #login(request.POST['username'])
            # redirect, or however you want to get to the main view
            return HttpResponseRedirect('login')
    else:
        form = UserForm() 

    return render(request, 'u_new.html', {'form': form}) 

# this login required decorator is to not allow to any  
# view without authenticating
@login_required(login_url="login/")
def login(request):
    return render(request="login.html")

# Display glucometer records
def post_list(request):
    if request.user.is_authenticated:
        list = G.objects.filter(id_p=request.user).order_by('datetime')
        return render(request, 'post_list.html', {'list': list})
    else:
        return render(request,"registration/forbidden.html")

# Adds glucometer records
def g_new(request):
        if request.method == "POST":
            form = GForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.id_p = request.user
                post.save()
                return redirect('/list', {'list': list})
        else:
            form = GForm()
        return render(request, 'g_edit.html', {'form': form})

# Displays chart based on gucometer recors
def chart2(request, chartID = 'chart_ID', chart_type = 'line', chart_height = 500):
    
    if request.user.is_authenticated:
        user = request.user
        data = ChartData.check_g_data(user)
        chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}  
        title = {"text": 'Control Glucemia'}
        xAxis = {"title": {"text": 'Fecha / Hora'}, "type": 'datetime', "dateTimeLabelFormats": {"month": "%e. %b", "year": "%b"}, "units": [['day', [1,5,10,15,20,25,30]], ['month',[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]], ['year', 'null']]}
    #    xAxis = {"title": {"text": 'Fecha / Hora'}, "type": 'linear'}
        yAxis = {"title": {"text": 'Glucometer display'}}
        series = [
            {"name": 'Fecha / Hora', "data": data['datax'] }, 
            {"name": 'Lectura', "data": data['value']},
            {"name": 'Promedio movil', "data": data['media']}
            ]
    
        return render(request, 'chart2.html', {'chartID': chartID, 'chart': chart,
                   'series': series, 'title': title,  'xAxis': xAxis, 'yAxis': yAxis})
    else:
        return render(request,"registration/forbidden.html")


# Class used by chart2 view
class ChartData(object):    
    def check_g_data(user):
        data = {'datax': [], 'value': [],'media': []}

        set = G.objects.filter(id_p=user).order_by('datetime')
        #limit = time.mktime(datetime.datetime.strptime(set[0].datetime, '%Y-%m-%d %H:%M:%S').timetuple())

        for record in set:
            #data['datetime'].append(record.datetime)
            #data['datax'].append(time.mktime(datetime.datetime.strptime(record.datetime, '%Y-%m-%d %H:%M:%S').timetuple()) - limit )
            data['datax'].append("Date(" + record.datetime[0:4] +", " + str(int(record.datetime[5:7]) - 1) + ", " + record.datetime[8:10] + ", " + record.datetime[11:13] + ", " + record.datetime[14:16] +  ",0,0)")
            data['value'].append(record.value)
            data['media'].append((len(data['value']) < 30) and sum(data['value']) / float(len(data['value'])) or (sum(data['value']) / float(len(data['value']))) )

        return data

# Displays guest page    
def guest(request):
    return render(request,"guest.html")

def forbidden(request):
    return render(request,"registration/forbidden.html")
