from django.urls import path, include
from . import views

app_name = 'customer'

urlpatterns = [
    path("", views.index, name='index'),
    path("transposed_list", views.transposed_list, name='transposed_list')

]
