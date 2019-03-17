from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('question', views.question, name='question'),
    path('ask', views.ask, name='ask'),
    path('tag', views.tag, name='tag'),
    path('profile', views.profile, name='profile'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
]
