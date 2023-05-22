from rest_framework import serializers

from apps.users.models import User
from apps.tasks.serializer import ToDoSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'created_at', 'age']

class UserDetailSerializer(serializers.ModelSerializer):
    user_tasks = ToDoSerializer(many=True, read_only=True)
    class Meta:
        model =User
        fields = ['id', 'username', 'email', 'phone_number', 'created_at', 'age']

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=100, write_only=True
    )
    password2 = serializers.CharField(
        max_length=100, write_only=True
    )
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'created_at', 'age', 'password', 'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password' : 'Пароли отличаются'})
        if '+996' not in attrs['phone_number']:
            raise serializers.ValidationError('Номер телефона должен быть в формате +996XXXXXXXXX')
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            phone_number = validated_data['phone_number'],
            age = validated_data['age']
        )
        user.set_password(validated_data['password2'])
        user.save()
        return user