from rest_framework import serializers
from users.models import Users

class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = [ 'name', 'familia', 'mail', 'login', 'parol']
