from django.urls import path, include
from .views import index, by_teacher, by_class


urlpatterns = [
    path('', index, name = 'index'),
    path('teacher/<str:teacher>', by_teacher, name = 'by_teacher'),
    path('class/<str:clas>', by_class, name = 'by_class'),
]