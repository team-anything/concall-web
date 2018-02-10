from django.conf.urls import url
from . import views

app_name = 'issues'

urlpatterns = [
    # url(r'^signup/$',views.signup_view,name = "signup"),
    # url(r'^login/$', views.login_view, name="login"),
    # url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^(?P<issueid>[\w-]+)/$',views.issue_detail, name="issue_detail"),
    url(r'^(?P<issueid>[\w-]+)/remove_issue$',views.remove_issue, name="remove_issue"),
    #url(r'^(?P<issueid>[\w-]+)/add_issue$',views.issue_add, name="issue_add")
]
