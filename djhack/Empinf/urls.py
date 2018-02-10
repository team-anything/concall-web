from django.conf.urls import url
from . import views

app_name = 'Empinf'

urlpatterns = [
    url(r'^home/$', views.home, name="home"),
    #url(r'^create/$', views.article_create, name="create"),
    url(r'^(?P<slug>[\w-]+)/$', views.emp_detail, name="detail"),
]
