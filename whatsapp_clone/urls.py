"""
URL configuration for whatsapp_clone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from chat.views import index,chatPage,signin,Filter,autocomplete_username,Personals,Create,Update,Delete,signup,signout
from whatsapp_clone import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    ####### registration
path('signup/',signup,name='signup'),
    path('',signin,name='signin'),
path("signout/", signout, name='signout'),

     path('index/',index,name='home'),
    path('<str:username>',chatPage,name='chat'),
path('autocomplete-username/', autocomplete_username, name='autocomplete_username'),
path('search/', Filter.as_view(), name='search'),
    ###### dp creation
path('list/', Personals.as_view(), name='list'),
path('create/', Create.as_view(), name='create'),
path('update/<int:pk>/',Update.as_view(),name='update'),
path('delete/<int:pk>/',Delete.as_view(),name='delete'),

####### group chat


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






