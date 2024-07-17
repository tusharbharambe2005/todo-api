from django.shortcuts import render
from rest_framework import viewsets,routers
from .models import User_model,tudo_list_model
from .serializers import UserSerializer,Tudo_list_serialize
from rest_framework.decorators import action
from rest_framework.response import Response


class UserViewset(viewsets.ModelViewSet):
    queryset = User_model.objects.all()
    serializer_class =UserSerializer 
    #/User_tudo/{user_tudo_id}/tudo_lists/
    @action(detail=True, methods=['get'])
    def tudo_lists(self,request,pk=None):
        try:
            UserIdUrl=User_model.objects.get(pk=pk)
            usj=tudo_list_model.objects.filter(user_tudo_relation=UserIdUrl)
            usj_seri=Tudo_list_serialize(usj,many=True,context={'request':request})
            return Response(usj_seri.data)
        except Exception as e:
            print(e)
            return Response({'massage':"User not difine"})

class tudo_list_Viewset(viewsets.ModelViewSet):
    queryset = tudo_list_model.objects.all()
    serializer_class=Tudo_list_serialize
# Create your views here.
