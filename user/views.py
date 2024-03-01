from django.shortcuts import render,redirect
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import UserSerializer,DivisionSerializer,DistrictSerializer
from .models import UserModel,Division,District
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from . paginations import UserPagination
from rest_framework.decorators import api_view

from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
class UserRegistration(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    pagination_class=UserPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['email', 'blood_group','division','District']
    
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("success")
        return Response(serializer.errors)
    
def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
    except(User.DoesNotExist):
        user = None 
    
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('https://github.com/')
    else:
        return redirect('https://github.com/')
    
    
class DivisionsView(APIView):
    def get(self,request):
        queryset=Division.objects.all()
        serializer=DivisionSerializer(queryset,many=True)
        return Response(serializer.data)
    

@api_view(['GET'])
def DivisionView(request,pk):
    queryset=Division.objects.get(pk=pk)
    serializer=DivisionSerializer(queryset)
    return Response(serializer.data)

class DistrictsView(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['division']
    # def get(self,request):
    #     queryset=District.objects.all()
    #     serializer=DistrictSeralizer(queryset,many=True)
    #     return Response(serializer.data)
    

@api_view(['GET'])
def DistrictView(request,pk):
    queryset=District.objects.get(pk=pk)
    serializer=DistrictSerializer(queryset)
    return Response(serializer.data)

    
