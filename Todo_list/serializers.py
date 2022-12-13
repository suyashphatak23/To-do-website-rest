from rest_framework import serializers
from .models import Task
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from datetime import date


class TaskSerializer(serializers.ModelSerializer):
    # Creating data formats for serializers
    id = serializers.IntegerField(read_only=True)
    record_date = serializers.DateField(read_only=True)
    record_time = serializers.TimeField(read_only=True)
    title = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    due_date = serializers.DateField(default=date.today)
    tag = serializers.ListField()
    status = serializers.CharField(default="OPEN")


    class Meta:
        model = Task
        fields = ('id','record_date', 'record_time', 'title', 'description', 'due_date', 'tag', 'status')

    
    def validate(self, data):
        if data['due_date']<data['record_date']:
            raise serializers.ValidationError({'error': "Due date should be greater than Creation date"})

class LoginSerializer(serializers.Serializer):
    """
    This serializer defines two fields used for authentication: username and password.
    It will try to authenticate the user with username/password when validated.
    """
    username = serializers.CharField(
        label="Username",
        write_only=True
    )
    password = serializers.CharField(
        label="Password",
        style={'input_type': 'password'},  # This will be used when the DRF browsable API is enabled
        trim_whitespace=False,
        write_only=True
    )

    def validate(self, attrs):
        # Take username and password from request
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            # Try to authenticate the user using Django auth framework.
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                # If we don't have a regular user, raise a ValidationError
                msg = 'Access denied: wrong username or password.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Both "username" and "password" are required.'
            raise serializers.ValidationError(msg, code='authorization')
        # We have a valid user, put it in the serializer's validated_data.
        # It will be used in the view.
        attrs['user'] = user
        return attrs


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
        ]