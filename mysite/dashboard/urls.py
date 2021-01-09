from django.urls import path

from . import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('claims/submit/', views.submit, name='submit'),
    path('claims/manage/<int:claim_id>', views.manage, name='manage'),
    path('claims/manage/<int:claim_id>/delete', views.delete, name='delete'),
]