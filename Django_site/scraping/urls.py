from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.Index().index_form, name='index'),
]
