from rest_framework.serializers import ModelSerializer

from .models import User

class UserSignUpSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['email'],validated_data['password'],
            **{
                'university': validated_data['university'],
            })
        user.save()
        return user

class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['email','nick_name']