from django.urls import path
from .views import home, dashboard, leaderboard

urlpatterns = [

    path(
        '',
        home,
        name='home'
    ),

    path(
        'dashboard/',
        dashboard,
        name='dashboard'
    ),

    path(
        'leaderboard/',
        leaderboard,
        name='leaderboard'
    ),

]