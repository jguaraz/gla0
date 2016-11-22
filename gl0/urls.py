from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^g/new/$', views.g_new, name='g_new'),
    url(r'^chart1$', views.chart1, name='chart1'),
    #url(r'^chart_data_json/', views.chart_data_json, name = 'chart_data_json'),
    url(r'^chart2$', views.chart2, name = 'chart2'),
]
