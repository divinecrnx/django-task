from django.urls import path

from . import views

app_name = 'logout'
urlpatterns = [
    path('', views.LogoutView.as_view(), name='index')
]