from django.conf import urls
from django.urls import path
from . import views

# SETTING UP THE NAMESPACE FOR TEMPLATE TAGGING
app_name = 'basicapp'

urlpatterns= [
    path('index/', views.index, name='index'),
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other')
]