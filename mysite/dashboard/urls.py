from django.urls import path

from . import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.index, name='index'),
    path('claims/submit/', views.submit, name='submit'),
    path('claims/manage/<int:id>', views.manage, name='manage')
]