import json,jwt
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer,TokenRefreshSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from config.settings import SECRET_KEY

@api_view(['GET'])
def token_refresh(request):
    refresh = request.META.get('HTTP_AUTHORIZATION',False)[7:]
    if refresh:
        try:
            refresh = RefreshToken(refresh)
            access = refresh.access_token
            return Response(
                {
                    "token": 
                        {
                            'access': str(access),
                            'refresh': str(refresh)
                        }
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': 'Invalid refresh token'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message': 'Refresh token not provided'}, status=status.HTTP_400_BAD_REQUEST)


class SignupView(APIView):
    def post(self, request):
        data             = json.loads(request.body)
        try:
            
            serializer_class = UserSignUpSerializer(data=data)
            if serializer_class.is_valid():
                # univ = request.body.get('HTTP_AUTHORIZATION',False)
                # if univ:
                #     university = get_object_or_404(University, pk=data['university'])
                #     serializer_class.save(university=university)
                # else:
                    
                serializer_class.save()
                return Response({
                        "message": "Signup Success"
                    },
                    status = status.HTTP_200_OK)
            return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
        except KeyError:
            return Response({"message":"KEY_ERROR"}, status = status.HTTP_400_BAD_REQUEST)
        
class UserAPIView(APIView):
    # 토큰으로 로그인
    def get(self, request):
        try:
            token = request.META.get('HTTP_AUTHORIZATION',False)[7:]
            if token:
                token = str(token).encode("utf-8")
            access = token
            payload = jwt.decode(access,SECRET_KEY,algorithms=['HS256'])
            pk = payload.get('user_id')
            user = get_object_or_404(User, pk=pk)
            serializer = UserModelSerializer(instance=user)
            return Response({'user':serializer.data}, status=status.HTTP_200_OK)
        except(jwt.exceptions.ExpiredSignatureError):
            return Response({"message" : "You need to refresh"},status=status.HTTP_400_BAD_REQUEST)
            
    # id pw 로 로그인
    def post(self, request):
        user = authenticate(
            username=request.data.get("email"), password=request.data.get("password")
        )
        # 이미 회원가입 된 유저일 때
        if user is not None:
            # jwt 토큰 접근
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            
            return Response({
                "message": "Login Success",
                "token":{
                    "access":access_token,
                    "refresh":refresh_token
                }
                },status = status.HTTP_200_OK)
        else:
            return Response({"message": "Login Fail"},status=status.HTTP_400_BAD_REQUEST)
        
## 이메일 중복 api
@api_view(['POST'])
def checkDuplicatedEmail(request):
    data = json.loads(request.body)
    if User.objects.filter(email = data['email']).exists():
        return Response({
            "message": "Duplicated email"
            }, status=status.HTTP_400_BAD_REQUEST)
    return Response({
        "message": "Accepted"
        }, status=status.HTTP_200_OK)

## 비밀번호 찾기

## 닉네임 변경