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
from adminn import views
from django.conf.urls.static import static
from mysqlproject import settings


urlpatterns = [
             path('api_data/',views.api_data,name="main"),
             # path('create/',views.createMovie,name="main"),
             path('',views.viewMovie,name="view_all"),
             path('deletemovie/',views.deleteMovie,name="deletemovie"),
            path('updatemovie/',views.updatemovie,name="updatemovie"),
            path('save_update/',views.saveUpdate,name="save_update"),
            path('newmovie/',views.newmovie,name="newmovie"),
            path('save_movie/',views.save_movie,name="save_movie"),
            path('save_data/',views.saveData)
    # path('',views.imdb_data)
]
if settings.DEBUG:
 urlpatterns += static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)

