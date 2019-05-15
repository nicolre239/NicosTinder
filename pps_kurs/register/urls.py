from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^register/', views.register, name="register"),
    url(r'^reg_check/$', views.reg_check, name="reg_check"),
]