from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^likes/(?P<user_id>\w+)', views.likes, name="likes"),
    url(r'^delete_like/$', views.delete_like, name="delete_like"),
    url(r'^search_pairs/(?P<user_id>\w+)', views.search_pairs, name="search_pairs"),
]