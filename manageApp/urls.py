
from django.contrib import admin
from django.urls import path
from nembers.views import *
from rest_framework import routers
from django.conf.urls import include

router = routers.DefaultRouter()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('get_student/',get_student,name="get_student"),
    path('add_student/<str:id>',add_student,name="add_student"),
    path('update_student/<str:id>',update_student,name="update_student"),
    path('add_admin/',add_admin,name="add_admin"),
]
