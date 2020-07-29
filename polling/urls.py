from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('launch/<poll_id>', views.launch, name='launch'),
    path('unlaunch/<poll_id>', views.unlaunch, name='unlaunch'),
    path('edit/<poll_id>', views.edit, name="edit"),
    path('user/<user_id>', views.user, name='user'),
    path('vote', views.vote, name='vote'),
]