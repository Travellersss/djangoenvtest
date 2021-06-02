from django.urls import path
from . import views

##路由
urlpatterns = [
    path("",views.index,name="index")


]