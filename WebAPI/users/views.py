from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from users.models import Users
from users.serializers import UsersSerializer


class UsersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [permissions.IsAuthenticated]
