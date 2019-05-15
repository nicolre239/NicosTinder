from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^profile/(?P<user_id>\w+)', views.profile, name="profile"),
    url(r'^profile_change/(?P<user_id>\w+)', views.profile_change, name="profile_change"),
    url(r'^profile_watch/(?P<match_id>\w+)/(?P<user_id>\w+)', views.profile_watch, name="profile_watch"),
    url(r'^changes_save/$', views.changes_save, name="changes_save"),
]