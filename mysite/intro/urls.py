from django.urls import path

from  . import views

app_name="intro"


urlpatterns=[

    path('home/',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('settings/',views.settings,name="settings"),
    path('exit/',views.exit,name="exit"),

]