from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^login_check/$', views.login_check, name="login_check"),
    url(r'^', views.login, name="login"),
]