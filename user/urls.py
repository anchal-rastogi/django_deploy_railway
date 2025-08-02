from django.urls import path
from . import views

urlpatterns=[
    path("",views.index),
    path("index/",views.index),
    path("home/",views.home),
    path("about/",views.about),
    path("education/",views.education),
    path("experties/",views.experties),
    path("project/",views.project),
    path("contact/",views.contact),

    #in case of blank url function will call by default.

]