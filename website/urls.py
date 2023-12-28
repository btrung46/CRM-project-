from django.urls import path 
from . import views
urlpatterns = [
    path('home/',views.home,name='home'),
    path('logout/',views.logout_user,name='logout'),
    path('',views.login_user,name='login'),
]