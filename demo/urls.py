from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from demo import views as core_views


urlpatterns = [
    url(r'^$', core_views.tpcc, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^select/$', core_views.tpcc, name='tpcc'),
    url(r'^lead/$', core_views.lead, name='lead'),
]
