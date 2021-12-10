"""gym URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
from home.views import get_topics_ajax,test_ag
from home.views import LoginUser, RegisterUser
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path('home/', include('home.urls')),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('login/', LoginUser.as_view(), name='LoginUser'),
    path('register_user/', RegisterUser.as_view(), name="RegisterUser"),

    path('polls/', include('polls.urls')),
    path('get_topics_ajax/', get_topics_ajax, name="get_topics_ajax"),
    path('test_ag/', test_ag, name="test_ag"),
    path('admin/', admin.site.urls),
]