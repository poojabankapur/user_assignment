from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from app.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'password']
        extra_kwargs = {'password': {'write_only': True}}

        validate_password = make_password

        def get_count(self, obj):
            # Provided the user is logged:
            user_id = self.context['request'].user.id
            return user_id
