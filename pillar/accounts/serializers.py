from accounts.models import Customer, User
from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    
    class Meta:
        model = Customer
        fields = (
            'user_form'
        )

        