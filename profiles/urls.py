from django.conf.urls import url, include
from . import views

app_name = "profiles"
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^profile/$', views.userProfiles, name='profile'),
]
