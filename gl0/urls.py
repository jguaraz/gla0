from django.conf.urls import url, include
from django.contrib.auth import views, logout
from . import views
from .forms import LoginForm

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^list/$', views.post_list, name='post_list'),
    url(r'^g_new/$', views.g_new, name='g_new'),
    url(r'^login/$', views.login, {'template_name': 'login.html', 'authentication_form': LoginForm}, name='login'),
    url(r'^logout/$', views.logout, {'next_page': '/'}),
    url(r'^chart2$', views.chart2, name='chart2'),
    url(r'^guest$', views.guest, name='guest'),
    url(r'^u_new$', views.u_new, name='u_new'),
    url(r'^.*/$', views.forbidden, name='forbidden'),
]
