from django.shortcuts import render
from django.contrib.auth import authenticate
from .models import Trainer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import(
    HTTP_200_OK,HTTP_201_CREATED,HTTP_404_NOT_FOUND,HTTP_204_NO_CONTENT
)
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
# Create your views here.


class Signup(APIView):
    def post(self,request):
        #tell it that username field is actually email field
        request.data["username"] = request.data["email"]
        #takes each keyword arg (kwarg) from request body . create_user will hash our user password field
        trainer = Trainer.objects.create_user(**request.data)
        #pass in user model (trainer) into token. Token now gets saved
        token = Token.objects.create(user=trainer)
        #token.key is the actual string of the token.
        #let client know trainer created, show off token key (irl not doing this lol), as well as http 200
        return Response({"trainer":trainer.email, "token": token.key},status= HTTP_200_OK)


class Login(APIView):
    """user login"""
    def post(self,request):
        email = request.data.get("email")
        password = request.data.get("password")

        #takes password and applies hashing, then compares to one on database
        trainer = authenticate(username=email,password=password)
        if trainer:
            #get or create returns a tuple of the token as well as a boolean of whether is created or not
            #get_or_create: Keep in mind tokens expire after logout or after a certain time period. Even if a user is signed up he might not have any tokens.
            token,created = Token.objects.get_or_create(user=trainer)   
            return Response({"token":token.key,"trainer":trainer.email},status=status.HTTP_200_OK)
        else:
            return Response("No trainer matching credentials",status = status.HTTP_404_NOT_FOUND)

##??
class Info(APIView):
    ##for this view to work these arguments need to be met.
    #must be using token authentication
    authentication_classes = [TokenAuthentication]
    #isAuthenticated,isAdminUser, isAuthenticatedOrReadOnly,
    permission_classes = [IsAuthenticated]

    def get(self,request):
        return Response({"email":request.user.email})

class Logout(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
#
    def post(self,request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)