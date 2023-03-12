from nembers.models import ClassLevel
from nembers.models import Student
from nembers.models import Project
from nembers.models import Admin
from rest_framework import serializers

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class classLevelSerializers(serializers.ModelSerializer):
    class Meta:
        model=ClassLevel
        fields ='__all__'
        
class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class AdminSerializers(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'
        
class InfoStudent(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField()