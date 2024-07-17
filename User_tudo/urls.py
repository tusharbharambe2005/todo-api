from django.urls import path,include
from .views import UserViewset,tudo_list_Viewset
from rest_framework import routers
#/User_tudo/v1/user_tudos/3/tudo_lists/

router = routers.DefaultRouter()
router.register(r'user_tudos',UserViewset)
router.register(r'tudo_lists',tudo_list_Viewset)

urlpatterns = [
    path('',include(router.urls))

]
