from django.contrib import admin
from django.urls import path
from . import views
from .views import HelloView, DisplayView,filterView,  index

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('index/', index, name='index'),
    path('', views.index, name='index'),
     path('add/',HelloView.as_view(), name='add'),
    path('display/',DisplayView.as_view(),name='display'),
    path('filter/',filterView.as_view(), name='filter'),
   
]


