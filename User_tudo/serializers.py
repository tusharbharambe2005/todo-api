from rest_framework import serializers
from .models import User_model,tudo_list_model            

class UserSerializer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.ReadOnlyField()
    class Meta:
        model = User_model
        fields = '__all__'
        
class Tudo_list_serialize(serializers.HyperlinkedModelSerializer):
        tudo_id = serializers.ReadOnlyField()

        class Meta:
             model = tudo_list_model
             fields = "__all__"