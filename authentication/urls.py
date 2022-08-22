import imp
from django.urls import path
from .views import RegisterView,ListTodoAPIView
urlpatterns = [
    path('',ListTodoAPIView.as_view()),

    path('register', RegisterView.as_view())
]
