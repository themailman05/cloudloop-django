from django.conf.urls import url
from django.urls import path

from . import views


urlpatterns = [
    path('load-sessions',views.load_sessions),
    path('load-loops', views.load_loops),
    path('add-session',views.add_session),
]