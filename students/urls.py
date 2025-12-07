from django.urls import path
from .views import register, StudentList

urlpatterns = [
    path('register/', register, name='register'),
    path('list/', StudentList.as_view()),
]