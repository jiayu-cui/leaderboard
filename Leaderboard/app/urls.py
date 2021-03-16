from django.urls import path, include
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('upload/', views.upload, name='upload'),
    path('show/', views.show, name='show'),
]