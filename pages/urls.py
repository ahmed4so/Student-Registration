from django.urls import path
from .views import home,form,view,search
urlpatterns = [
    path('',home,name='Home'),
    path('form', form, name='Form'),
    path('students',view,name='students'),
    path('search', search, name='search')
]