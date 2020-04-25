from django.urls import path

from userauth import views

urlpatterns = [
    path('login',views.auth_login),
    path('logout',views.auth_logout),
    path('register',views.signup),
]
