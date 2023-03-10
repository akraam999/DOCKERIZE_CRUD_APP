from django.shortcuts import render
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework import permissions
from nembers.models import *
from nembers.serializers import *
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password

#GET STUDENTS 
@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_student(request):
    queryset = Student.objects.all()
    serializer = StudentSerializers(queryset,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

#ADD STUDENT
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def add_student(request):
    serializer = StudentSerializers(data=request.data)
    if(serializer.is_valid()):
        query = Student.objects.filter(email=request.data['email'])
        if(len(query)>0):
            content = {'error':'email deja existe !'}
            return Response(content,status=status.HTTP_400_BAD_REQUEST)
        else:
            password = request.data.get('password')
            password = make_password(password)
            user = Student.objects.create(first_name=request.data.get('first_name'),last_name=request.data.get('last_name'),email=request.data.get('email'),password=password,classLevel=request.data.get('classLevel'))
            serializer = StudentSerializers(user)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)

#UPDATE STUDENT
@api_view(['PUT'])
@permission_classes([permissions.AllowAny])
def update_student(request,id):
    query = Student.objects.filter(id=id)
    if(len(query)<=0):
        return Response({'error':'no user with this id !'},status=status.HTTP_400_BAD_REQUEST)
    serializer = StudentSerializers(query,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer. errors,status=status.HTTP_400_BAD_REQUEST)

#DELETE STUDENT
@api_view(['DELETE'])
@permission_classes([permissions.AllowAny])
def delete_student(request,id):
    query = Student.objects.filter(id=id)
    if(query):
        query.delete()
        return Response({"msg":"student has been delected !"},status=status.HTTP_202_ACCEPTED)
    else:
        return Response({'error':'no user with this id !'},status=status.HTTP_400_BAD_REQUEST)


#Add admin 
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def add_admin(request):
    query = Admin.objects.filter(email=request.data['email'])
    if (len(query)>0):
        return Response({'error':'admin already exist !'},status=status.HTTP_400_BAD_REQUEST)
    serializer = AdminSerializers(data=request.data)
    if serializer.is_valid:
        password = make_password(request.data.get('password'))
        admin = Admin.objects.create(username=request.data.get('username'),email=request.data.get('email'),password=password)
        serializer = AdminSerializers(admin)
        serializer.save()
        return Response({'status':'ok'},status=status.HTTP_200_OK)
    else:
        return Response({'status':'wrong request !'},status=status.HTTP_403_FORBIDDEN)

