"""mysqlproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from userapp import views

urlpatterns = [
    path("", views.userIndex,name="userhome"),
    path("user_signin/",views.user_signin,name="user_signin"),
    path("trailer_play/",views.trailer_play,name="trailer_play"),
    path("search/",views.search,name="search"),
    path("watch_list_page/",views.watch_list_page,name="watch_list_page"),
    path("add_to_watchlist/",views.add_to_watchlist,name="add_to_watchlist"),

]

