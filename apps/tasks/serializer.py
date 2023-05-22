from rest_framework import serializers

from apps.tasks.models import ToDo

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ['title', 'description', 'image']

class TaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'