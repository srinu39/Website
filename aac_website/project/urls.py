from django.urls import path
from project import views

app_name = 'project'
urlpatterns = [
    path('',views.indexView, name='index')
]