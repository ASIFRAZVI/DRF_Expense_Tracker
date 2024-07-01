from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import auth_serializer, login_serializer
from .models import CustomUser
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.permissions import IsAuthenticated, AllowAny
from .jwt_token.token_genarator import generate_jwt_token,generate_refresh_token
from.jwt_token.token_decoder import decode_jwt_token

class Registration(APIView):
    """ Register a new user. """
    permission_classes=[AllowAny]

    def post(self, request):
        user_serializer=auth_serializer(data=request.data)
        password = request.data.get('password')
        request.data['password'] = make_password(password) 

        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'ok':'sucussfully user registered' }, status=status.HTTP_201_CREATED)
        else:
            return Response({'errors': 'Error while registration', 'errors': user_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
class Login(APIView):
    """Function to login user"""
    permission_classes=[AllowAny]

    def post(self, request):
        signin_serializer= login_serializer(data=request.data)
        

        if signin_serializer.is_valid(): 
            username = signin_serializer.validated_data.get('username')
            password = signin_serializer.validated_data.get('password')
        
            try:
                user = CustomUser.objects.get(username=username)
            except CustomUser.DoesNotExist:
                return Response({'error': 'Invalid username'}, status=400)
            
            if check_password(password, user.password):
             
                #generate access main token
                jwt_token = generate_jwt_token(user.id, 'asifrazasecratestoreinenv')

                # Generate refresh token
                refresh_token = generate_refresh_token(user.id, 'asifrazasecratestoreinenv')    

                response=Response({
                    'token': jwt_token,
                    'refresh_token': refresh_token,
                    "ok":"redirectiong to dasboard",
                    },status=200)
                    
            
                # Set token in cookies
                response.set_cookie('access_token', jwt_token, httponly=True)
                response.set_cookie('refresh_token', refresh_token, httponly=True)

                return response

            else:
                return Response({"error":"invalid password!"}, status=400)

        else:
            return Response(signin_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class DashboardView(APIView): 
    """function for final redirection"""

    def get(self, request):
        try:
            token = decode_jwt_token(request, 'asifrazasecratestoreinenv')
            user_id = token.get('user_id')
            
            try:
                # Query the user using the user_id
                user = CustomUser.objects.filter(id=user_id).first()
            except:
                return Response({"error": "User not found"}, status=404)

            # print(user.password)

            return Response({"token": token}, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=400)


