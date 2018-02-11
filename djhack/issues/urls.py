from django.conf.urls import url
from . import views

app_name = 'issues'

urlpatterns = [
    # url(r'^signup/$',views.signup_view,name = "signup"),
    # url(r'^login/$', views.login_view, name="login"),
    url(r'^add_issue/$', views.add_issue, name="add_issue"),
    url(r'^(?P<issueid>\d+)/$',views.issue_detail, name="issue_detail"),
    url(r'^(?P<issueid>\d+)/remove_issue$',views.remove_issue, name="remove_issue"),
    #url(r'^(?P<issueid>[\w-]+)/add_issue$',views.issue_add, name="issue_add")
]
