from django.urls import path
from . import views


urlpatterns = [

    path("", views.home, name="home"),

    path('tweet_list', views.tweet_list, name='tweet-list'),

    path('create/', views.tweet_create, name='tweet-create'),

    path('<int:tweet_id>/edit/', views.tweet_edit, name='tweet-edit'),

    path('<int:tweet_id>/delete/', views.tweet_delete, name='tweet-delete'),

    path('register/', views.register, name='register'),
]
