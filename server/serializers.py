from rest_framework import serializers
from django.contrib.auth.models import User

### Un Serializer podria compararse a aun DTO
# Aprovechamos el User Model que ya biene con django en esta ocasion
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'username', 'email', 'password']