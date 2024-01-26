from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('signout', views.signout, name='signout'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('back', views.back, name='back')
]
