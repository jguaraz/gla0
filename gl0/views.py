from django.shortcuts import render, redirect
from django.utils import timezone
#from chartit import DataPool, Chart
from .models import G
from .forms import GForm
# Create your views here.
def post_list(request):
    list = G.objects.filter(datetime__lte=timezone.now()).order_by('datetime')
    return render(request, 'gl0/post_list.html', {'list': list})

def g_new(request):
        if request.method == "POST":
            form = GForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                '''post.author = request.user
                post.published_date = timezone.now() '''
                post.save()
                return redirect('/', {'list': list})
        else:
            form = GForm()
        return render(request, 'gl0/g_edit.html', {'form': form})

'''
def chart1(request):
    # Datapool
    data = DataPool( series=[{'options': {'source': G.objects.all().order_by('datetime') },
                            'terms': ['datetime','value']}]  )
    # chart
    cht = Chart( datasource = data,
                 series_options = [ {'options':{
                     type: 'line',
                     'stacking': False }, 'terms': {'datetime' : ['value']}  }],
                 chart_options =
                    { 'title': {'text': 'Control de Glucemia'},
                     'xAxis': {'title': {'text': 'Fecha/Hora'} } } 
                 )
    #Step 3: Send the PivotChart object to the template.
    return render_to_response({'chart1': cht})
'''    
def chart1(request):
    return render(request, 'gl0/chart1.html')

def chart2(request, chartID = 'chart_ID', chart_type = 'line', chart_height = 500):
    data = ChartData.check_g_data()

    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}  
    title = {"text": 'Control Glucemia'}
    xAxis = {"title": {"text": 'Fecha / Hora'}}
    yAxis = {"title": {"text": 'Data'}}
    series = [
        {"name": 'Fecha / Hora', "data": data['datetime']}, 
        {"name": 'Lectura', "data": data['value']},
        {"name": 'Promedio movil', "data": data['media']}
        ]

    return render(request, 'gl0/chart2.html', {'chartID': chartID, 'chart': chart,
                                                    'series': series, 'title': title, 
                                                    'xAxis': xAxis, 'yAxis': yAxis})



class ChartData(object):    
    def check_g_data():
        data = {'datetime': [], 'value': [],
                 'media': []}

        set = G.objects.all()

        for record in set:
            data['datetime'].append(record.datetime)
            data['value'].append(record.value)
            data['media'].append((len(data['value']) < 30) and sum(data['value']) / float(len(data['value'])) or (sum(data['value']) / float(len(data['value']))) )

        return data