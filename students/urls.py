from django.urls import path
from .views import register, StudentList

urlpatterns = [
    path('', register, name='register'),
    path('list/', StudentList.as_view()),
]